---
symbol: "SLC6A13"
type: "gene"
col: 209
ensembl_id: "ENSG00000010379"
name: "solute carrier family 6 member 13"
location: "12p13.33"
module: 39
arm: "+"
pooled_cpm: 4.54
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# SLC6A13

*solute carrier family 6 member 13* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.04× (z +14.5, q 7e-45, up in 39 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.403× (z -5.8, q 3e-06, down in 24 of 46 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.435× (z -5.3, q 3e-05, down in 25 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYOCOS]] (+0.88, fdr 7e-06), [[GARIN1A]] (+0.87, fdr 7e-06), [[USP50]] (+0.87, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 209.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.04×** | +14.5 | 7e-45 | 39/39 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **7.65×** | +12.9 | 1e-35 | 44/45 (HOP62, SW480, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.93×** | +12.2 | 3e-32 | 33/39 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.89×** | +10.8 | 5e-25 | 31/35 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.69×** | +9.4 | 5e-19 | 34/38 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.84×** | +8.5 | 2e-15 | 27/38 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.20×** | +7.0 | 2e-10 | 26/46 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **2.53×** | +5.9 | 3e-07 | 30/46 (HOP62, A498, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.26×** | +5.1 | 2e-05 | 17/47 (NCI-H23, A-427, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.69×** | +4.7 | 2e-04 | 19/45 (NCI-H2347, NCI-H460, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.15×** | +4.6 | 3e-04 | 18/44 (A-427, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.16×** | +4.5 | 4e-04 | 4/12 (HOP62, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +3.7 | 0.008 | 0/7 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.85×** | +3.7 | 0.008 | 16/45 (LoVo, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 209.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.403×** | -5.8 | 3e-06 | 24/46 (H4, NCI-H23, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.435×** | -5.3 | 3e-05 | 25/44 (H4, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.470×** | -4.9 | 2e-04 | 23/34 (NCI-H23, A498, …) | all doses, stronger at high dose | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.252×** | -4.6 | 6e-04 | 17/33 (KATO III, SW 900, …) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.496×** | -4.5 | 8e-04 | 18/44 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.361×** | -3.4 | 0.055 | 11/26 (SW 900, NCI-H2030, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.573×** | -3.4 | 0.055 | 16/42 (SW1417, NCI-H23, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.693×** | -3.4 | 0.055 | 15/44 (NCI-H1792, MIA PaCa-2, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.612×** | -3.2 | 0.095 | 14/42 (H4, SW 900, …) | all doses, stronger at high dose | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | 0.617× | -3.1 | 0.10 | 15/45 (HepG2/C3A, COLO 205, …) | rises with dose |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.610× | -3.1 | 0.11 | 14/44 (RPMI-7951, C32, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 209. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 18.0 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0161× (z -14.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0389× (z -11.1) |
| [[SW480 (line)]] | alt | 2.50 | 5 | 0 | [[Auranofin (drug)]] 5 µM 23.1× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 4.12 | 4 | 0 | [[Auranofin (drug)]] 5 µM 58.2× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 1 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 12.5× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.0700× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LoVo (line)]] | wt | 5.62 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +10.6) | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0686× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 5.84 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 1.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 49.6× (z +8.5) | — |
| [[HCT15 (line)]] | alt | 4.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 8.78 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0719× (z -9.1) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 7.68 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0599× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~92% of this change |
| [[NCI-H460 (line)]] | wt | 2.89 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.62× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 1.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +8.7) | — |
| [[A-172 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.74 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 209), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYOCOS]] | +0.88 | +0.88 / +0.80 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.87 | +0.85 / +0.80 | both halves | 7e-06 |  |
| [[USP50]] | +0.87 | +0.90 / +0.80 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.87 | +0.87 / +0.80 | both halves | 7e-06 |  |
| [[ALDH8A1]] | +0.87 | +0.90 / +0.80 | both halves | 7e-06 |  |
| [[GARIN1B]] | +0.86 | +0.87 / +0.80 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.84 | +0.84 / +0.74 | both halves | 7e-06 |  |
| [[DPYS]] | +0.83 | +0.82 / +0.76 | both halves | 7e-06 |  |
| [[MPP4]] | +0.83 | +0.87 / +0.75 | both halves | 7e-06 |  |
| [[LINC00393]] | +0.82 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.82 | +0.80 / +0.81 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.81 | +0.85 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC6A13's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[XG]] | B | XG activity raises SLC6A13's level | lines that do not express XG (5) vs lines expressing it (45) | 2.08× lower at baseline in the lines without XG | 0.024 | ⚠ within organs, on part of the lines; also absent: TXNRD3, FSCN1, ELK3; maybe low, not absent |
| [[DYSF]] | B | DYSF activity raises SLC6A13's level | lines that do not express DYSF (11) vs lines expressing it (39) | 1.81× lower at baseline in the lines without DYSF | 0.058 | ⚠ within organs, on part of the lines; also absent: ISM2, IRX3, DNAAF9; maybe low, not absent |
| [[NEK10]] | B | NEK10 activity raises SLC6A13's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.05× lower at baseline in the lines without NEK10 | 0.059 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[LINC00334]] | B | LINC00334 activity raises SLC6A13's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.85× lower at baseline in the lines without LINC00334 | 0.076 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |
| [[ASGR1]] | B | ASGR1 activity raises SLC6A13's level | lines that do not express ASGR1 (9) vs lines expressing it (41) | 1.43× lower at baseline in the lines without ASGR1 | 0.093 | ⚠ within organs, on part of the lines; also absent: PRDM6, ENSG00000288993, ADAM22; maybe low, not absent |
| [[GARIN1B]] | C | GARIN1B activity raises SLC6A13's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 2.41× lower at baseline in the lines without GARIN1B | 0.059 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.930). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.8, -13.4); signed map (18.0, 8.4). **Vector** length 101, 22.8% of its response variance represented; |z| ≥ 3 in 1,373 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.9 | +12.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +14.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.5 | +12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +8.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +10.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +7.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +5.0 | +4.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +5.0 | +5.9 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +2.6 | +2.4 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.5 | -3.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -0.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.1 | -1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.1 | -5.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -3.6 | -3.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 6 member 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:220,621-262,873 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GAT2 |
| Gene groups (HGNC) | Solute carrier family 6 |
| Reactome | 7 pathways, smallest: SLC-mediated transport of neurotransmitters; GABA synthesis, release, reuptake and degradation; Neurotransmitter release cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSD5](https://www.uniprot.org/uniprotkb/Q9NSD5) (Sodium- and chloride-dependent GABA transporter 2):

> Mediates sodium- and chloride-dependent transport of gamma-aminobutyric acid (GABA). Mediates transport of beta-alanine. Can also mediate transport of taurine and hypotaurine (By similarity).

**Summary**, from NCBI Gene [6540](https://www.ncbi.nlm.nih.gov/gene/6540):

> Enables gamma-aminobutyric acid:sodium:chloride symporter activity. Involved in amino acid import across plasma membrane and monocarboxylic acid transport. Located in mitochondrion and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:11046](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11046) · Entrez [6540](https://www.ncbi.nlm.nih.gov/gene/6540) · UniProt [Q9NSD5](https://www.uniprot.org/uniprotkb/Q9NSD5) · Ensembl [ENSG00000010379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000010379)

## Data

Gene col 209: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 209); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 209, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 209]; `tensor/DDL_lfc|DDL_z.npy` [209]; `embed/gene_vectors.npy` [209]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 209 or target_col == 209). Every well: [[SLC6A13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC6A13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
