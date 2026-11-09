---
symbol: "DISP3"
type: "gene"
col: 12906
ensembl_id: "ENSG00000204624"
name: "dispatched RND transporter family member 3"
location: "1p36.22"
module: 165
arm: "+"
pooled_cpm: 2.23
n_lines_expressing: 43
n_dd_up: 29
n_dd_down: 4
n_dd_up_clean: 22
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 2
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# DISP3

*dispatched RND transporter family member 3* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 11.9× (z +29.2, q 0e+00, up in 22 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.578× (z -4.6, q 0.002, down in 10 of 28 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL23A1]] (+0.65, fdr 1e-05), [[TMEM132B]] (+0.64, fdr 7e-06), [[NPTX2]] (+0.63, fdr 7e-06); moves opposite to [[IQCK]] (-0.51, fdr 5e-04), [[DNAJC16]] (-0.49, fdr 2e-04), [[OTUD6B]] (-0.47, fdr 2e-04).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NPTXR]] → it (grade B ⚠); 2 go from it, the strongest it → [[CELF5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12906.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **11.9×** | +29.2 | 0e+00 | 22/23 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **13.1×** | +21.5 | 0e+00 | 35/35 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **8.48×** | +17.9 | 0e+00 | 33/33 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **4.43×** | +17.6 | 0e+00 | 36/36 (SW480, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.06×** | +13.2 | 9e-38 | 16/26 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **4.83×** | +13.2 | 1e-37 | 29/32 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **4.79×** | +12.6 | 2e-34 | 12/18 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.51×** | +10.1 | 5e-22 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.09×** | +9.4 | 3e-19 | 30/36 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.06×** | +9.3 | 5e-19 | 23/28 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.14×** | +9.0 | 1e-17 | 11/35 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.93×** | +8.6 | 3e-16 | 14/23 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **2.64×** | +7.8 | 3e-13 | 5/9 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.37×** | +7.2 | 3e-11 | 2/8 (SW480, NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.78×** | +6.8 | 5e-10 | 12/35 (J82, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.12×** | +6.3 | 1e-08 | 19/31 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +4.8 | 5e-05 | 9/32 (NCI-H2347, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.78×** | +4.8 | 5e-05 | 10/26 (SW480, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12906.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.578×** | -4.6 | 0.002 | 10/28 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.597×** | -4.3 | 0.004 | 8/36 (PANC-1, H4, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.620×** | -4.0 | 0.011 | 12/31 (HepG2/C3A, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.740×** | -3.6 | 0.047 | 9/32 (NCI-H2030, J82, …) | top dose only |  |
| [[Diphenhydramine (drug)]] 5 µM |  | 0.671× | -3.2 | 0.14 | 7/32 (NCI-H460, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12906. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 2.06 | 5 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.5× (z +14.9) | [[Digitoxin (drug)]] 5 µM 0.0902× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 3.43 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.8× (z +15.8) | — |
| [[SW1417 (line)]] | alt | 6.81 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.07× (z +8.8) | [[Menadione (drug)]] 5 µM 0.0735× (z -9.7) |
| [[HOP62 (line)]] | alt | 5.20 | 0 | 2 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0723× (z -9.2) ⚠ toxic · without an alert: [[Cobimetinib (drug)]] 0.05 µM 0.0716× (z -8.5) |
| [[A-427 (line)]] | wt | 7.33 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 12.8× (z +10.5) | — |
| [[A549 (line)]] | wt | 1.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 35.3× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 5.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.7× (z +9.0) | — |
| [[HEC-1-A (line)]] | alt | 0.592 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 50.0× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 0.973 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 28.4× (z +8.9) | — |
| [[J82 (line)]] | alt | 1.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.2× (z +9.6) | — |
| [[LoVo (line)]] | wt | 4.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.65× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.31 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 21.5× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 3.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.91× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 0.807 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 29.9× (z +10.9) | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.120× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~77% of this change |
| [[A-172 (line)]] | wt | 0.580 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.749 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.618 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.698 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.399 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.740 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.211 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.332 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.862 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.816 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.246 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.577 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.615 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.57 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12906), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL23A1]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[TMEM132B]] | +0.64 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[NPTX2]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[KCNB1]] | +0.61 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[CDH23]] | +0.60 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[SYN1]] | +0.60 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[MTUS2]] | +0.60 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[PLD5]] | +0.59 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[ATP6V1C2]] | +0.59 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[HAP1]] | +0.58 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PPP1R14C]] | +0.58 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[SMPD3]] | +0.58 | +0.61 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQCK]] | -0.51 | -0.23 / -0.54 | both halves | 5e-04 |  |
| [[DNAJC16]] | -0.49 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[OTUD6B]] | -0.47 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[AAGAB]] | -0.47 | -0.46 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPTXR]] | B | NPTXR activity raises DISP3's level | lines that do not express NPTXR (11) vs lines expressing it (39) | 1.78× lower at baseline in the lines without NPTXR | 0.040 | ⚠ within organs, on part of the lines; also absent: WNT9A, RAB6B, MAPK8IP2; maybe low, not absent |
| [[AP3B2]] | B | AP3B2 activity raises DISP3's level | lines that do not express AP3B2 (15) vs lines expressing it (35) | 1.76× lower at baseline in the lines without AP3B2 | 0.041 | ⚠ within organs, on part of the lines; also absent: MAPK8IP2, MED12L, HRK; maybe low, not absent |
| [[KCNK13]] | B | KCNK13 activity raises DISP3's level | lines that do not express KCNK13 (9) vs lines expressing it (41) | 1.85× lower at baseline in the lines without KCNK13 | 0.042 | ⚠ within organs, on part of the lines; also absent: TMEM170B, TMEM145, LINC02609; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DISP3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CELF5]] | B | DISP3 activity raises CELF5's level | lines that do not express DISP3 (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without DISP3 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC02609, DPF1, ARHGEF26 |
| [[SORCS3]] | B | DISP3 activity raises SORCS3's level | lines that do not express DISP3 (7) vs lines expressing it (43) | 1.25× lower at baseline in the lines without DISP3 | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC02609, DPF1, ARHGEF26 |

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.653). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.2, 32.7); signed map (28.7, 19.2). **Vector** length 53.8, 8.59% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +17.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +10.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.9 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +29.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +9.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +1.6 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -0.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -3.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | dispatched RND transporter family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:11,479,155-11,537,551 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1337; previously PTCHD2 |
| Gene groups (HGNC) | Dispatched RND transporter family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2K9](https://www.uniprot.org/uniprotkb/Q9P2K9) (Protein dispatched homolog 3):

> Plays a role in neuronal proliferation and differentiation. Plays a role in the accumulation of cellular cholesterol (By similarity). Involved in intracellular lipid droplet formation. May contribute to cholesterol homeostasis in neuronal cells (By similarity).

**Summary**, from NCBI Gene [57540](https://www.ncbi.nlm.nih.gov/gene/57540):

> Involved in negative regulation of neuron differentiation; positive regulation of lipid metabolic process; and positive regulation of neural precursor cell proliferation. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29251](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29251) · Entrez [57540](https://www.ncbi.nlm.nih.gov/gene/57540) · UniProt [Q9P2K9](https://www.uniprot.org/uniprotkb/Q9P2K9) · Ensembl [ENSG00000204624](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204624)

## Data

Gene col 12906: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12906); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12906, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12906]; `tensor/DDL_lfc|DDL_z.npy` [12906]; `embed/gene_vectors.npy` [12906]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12906 or target_col == 12906). Every well: [[DISP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DISP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
