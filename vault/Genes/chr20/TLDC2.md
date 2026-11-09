---
symbol: "TLDC2"
type: "gene"
col: 2118
ensembl_id: "ENSG00000101342"
name: "TBC/LysM-associated domain containing 2"
location: "20q11.23"
module: 31
arm: "+"
pooled_cpm: 3.74
n_lines_expressing: 43
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 60
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# TLDC2

*TBC/LysM-associated domain containing 2* — 20q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.04× (z +14.5, q 8e-45, up in 10 of 24 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (COLO 205 0.0348×, SW480 0.0927×, LS 180 0.0716×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (CFPAC-1 0.182×, LS 180 0.187×, AsPC-1 0.272×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (SW480 0.0961×, LS 180 0.0671×; ⚠ cell-cycle shift, explains ~98% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HEC-1-A 0.0769×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LASTR]] (+0.69, fdr 7e-06), [[B3GNT3]] (+0.68, fdr 7e-06), [[LCK]] (+0.67, fdr 7e-06); moves opposite to [[TTC28]] (-0.49, fdr 5e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 60 arrows point to it, the strongest [[INAVA]], [[MROH3P]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2118.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.04×** | +14.5 | 8e-45 | 10/24 (A498, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.76×** | +13.8 | 5e-41 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.49×** | +8.4 | 8e-15 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +6.4 | 3e-08 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.52×** | +3.8 | 0.014 | 1/22 (SW1417) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.72×** | +3.6 | 0.035 | 1/20 (A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.44×** | +3.3 | 0.069 | 8/24 (SHP-77, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[palbociclib (drug)]] 5 µM |  | 1.87× | +3.0 | 0.15 | 0/18 | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.87× | +3.0 | 0.15 | 1/5 (SW480) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2118.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (COLO 205 0.0348×, SW480 0.0927×, LS 180 0.0716×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (CFPAC-1 0.182×, LS 180 0.187×, AsPC-1 0.272×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (SW480 0.0961×, LS 180 0.0671×; ⚠ cell-cycle shift, explains ~98% of this change); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HEC-1-A 0.0769×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.712× | -3.2 | 0.46 | 12/33 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.693× | -3.1 | 0.46 | 3/36 (NCI-H23, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2118. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 8.94 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0544× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0716× (z -10.0) |
| [[SW480 (line)]] | alt | 18.3 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0927× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 9.79 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0682× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 15.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -8.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.272× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 5.69 | 0 | 2 (1 ⚠) | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0769× (z -10.9) |
| [[COLO 205 (line)]] | alt | 15.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0348× (z -11.7) |
| [[A-172 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.788 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.906 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.917 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.901 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.852 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.974 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.840 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.943 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2118), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LASTR]] | +0.69 | +0.71 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[B3GNT3]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[LCK]] | +0.67 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[BLACAT1]] | +0.67 | +0.61 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[SLC5A1]] | +0.67 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[INAVA]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[LEMD1]] | +0.67 | +0.58 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[CRYBG2]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[HS3ST1]] | +0.65 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[PADI1]] | +0.64 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[LINC03040]] | +0.64 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[INPP5D]] | +0.63 | +0.51 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC28]] | -0.49 | -0.39 / -0.47 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*60 arrows, 60 of them with an alert ⚠; grade A 0, B 60, C 0. Shown: the 12 strongest; 48 more arrows (48 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[INAVA]], [[MROH3P]] | B | INAVA, MROH3P activity raises TLDC2's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 2.52× lower at baseline in the lines without INAVA, MROH3P | 1e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent genes |
| [[B3GNT3]] | B | B3GNT3 activity raises TLDC2's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 2.64× lower at baseline in the lines without B3GNT3 | 2e-04 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[CDH1]] | B | CDH1 activity raises TLDC2's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.65× lower at baseline in the lines without CDH1 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[EPS8L3]] | B | EPS8L3 activity raises TLDC2's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 3.19× lower at baseline in the lines without EPS8L3 | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A |
| [[LINC03040]] | B | LINC03040 activity raises TLDC2's level | lines that do not express LINC03040 (31) vs lines expressing it (19) | 2.66× lower at baseline in the lines without LINC03040 | 6e-04 | ⚠ within organs, on part of the lines; also absent: SLC44A4, EPS8L3, LCN2 |
| [[LINC02964]] | B | LINC02964 activity raises TLDC2's level | lines that do not express LINC02964 (38) vs lines expressing it (12) | 3.21× lower at baseline in the lines without LINC02964 | 7e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53, CDKN2A; also absent: CLRN3, GPA33, EPS8L3 |
| [[GPR35]] | B | GPR35 activity raises TLDC2's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 2.26× lower at baseline in the lines without GPR35 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[MOGAT3]] | B | MOGAT3 activity raises TLDC2's level | lines that do not express MOGAT3 (30) vs lines expressing it (20) | 2.11× lower at baseline in the lines without MOGAT3 | 0.002 | ⚠ within organs, on part of the lines; also absent: VIL1, LINC02964, LINC01819 |
| [[C1orf116]], [[IRF6]] | B | C1orf116, IRF6 activity raises TLDC2's level | lines that do not express C1orf116, IRF6 (31) vs lines expressing them (19) | 2.49× lower at baseline in the lines without C1orf116, IRF6 | 0.002 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS4, TMEM125; co-absent genes |
| [[ADCY4]] | B | ADCY4 activity raises TLDC2's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 2.37× lower at baseline in the lines without ADCY4 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[FGD5]] | B | FGD5 activity raises TLDC2's level | lines that do not express FGD5 (37) vs lines expressing it (13) | 2.33× lower at baseline in the lines without FGD5 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000265554, TFF2, KRT5 |
| [[HNF4A]] | B | HNF4A activity raises TLDC2's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.69× lower at baseline in the lines without HNF4A | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.0, 53.0); signed map (58.5, 11.7). **Vector** length 49.7, 8.07% of its response variance represented; |z| ≥ 3 in 761 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +14.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +13.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +6.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +1.3 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.9 | -0.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -2.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.6 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~98% of this change | -1.3 | -0.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.9 | -1.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[XRK3F2 (drug)]] 5 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | TBC/LysM-associated domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.23 — chr20:36,876,121-36,894,235 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ132F21.2; previously C20orf118 |
| Gene groups (HGNC) | TLDc domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [A0PJX2](https://www.uniprot.org/uniprotkb/A0PJX2) (TLD domain-containing protein 2):

> Inhibits the activity of the vacuolar-type ATPase (V-ATPase) by inducing disassembly of the V-ATPase complex. Protects neuronal cells against oxidative stress (By similarity). Required for kidney bicarbonate secretion (By similarity).

**Summary**, from NCBI Gene [140711](https://www.ncbi.nlm.nih.gov/gene/140711):

> Predicted to be involved in response to oxidative stress. Predicted to act upstream of or within negative regulation of cellular response to oxidative stress. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:16112](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16112) · Entrez [140711](https://www.ncbi.nlm.nih.gov/gene/140711) · UniProt [A0PJX2](https://www.uniprot.org/uniprotkb/A0PJX2) · Ensembl [ENSG00000101342](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101342)

## Data

Gene col 2118: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2118); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2118, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2118]; `tensor/DDL_lfc|DDL_z.npy` [2118]; `embed/gene_vectors.npy` [2118]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2118 or target_col == 2118). Every well: [[TLDC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLDC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
