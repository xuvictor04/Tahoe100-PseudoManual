---
symbol: "FAM24B"
type: "gene"
col: 13087
ensembl_id: "ENSG00000213185"
name: "family with sequence similarity 24 member B"
location: "10q26.13"
module: 77
arm: "+"
pooled_cpm: 12.8
n_lines_expressing: 42
n_dd_up: 20
n_dd_down: 10
n_dd_up_clean: 15
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# FAM24B

*family with sequence similarity 24 member B* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.89× (z +9.2, q 1e-17, up in 29 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.600× (z -7.1, q 6e-10, down in 12 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.724× (z -6.6, q 1e-08, down in 22 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF692]] (+0.67, fdr 7e-06), [[CDK5RAP1]] (+0.65, fdr 7e-06), [[SNU13]] (+0.65, fdr 1e-05); moves opposite to [[MED29]] (-0.63, fdr 1e-05), [[USP11]] (-0.63, fdr 1e-05), [[BAZ2B]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CUZD1]] → it (grade C ⚠); 1 goes from it, the strongest it → [[CUZD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13087.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.89×** | +9.2 | 1e-17 | 29/39 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.84×** | +8.8 | 2e-16 | 30/40 (NCI-H1573, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.84×** | +8.8 | 2e-16 | 29/37 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.77×** | +8.3 | 2e-14 | 27/40 (NCI-H1573, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +8.2 | 4e-14 | 25/39 (NCI-H1573, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.63×** | +7.3 | 2e-11 | 25/39 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.8 | 6e-07 | 22/40 (SNU-423, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +4.9 | 6e-05 | 16/38 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.40×** | +4.8 | 8e-05 | 14/39 (PANC-1, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.8 | 8e-05 | 16/33 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +4.7 | 2e-04 | 13/40 (NCI-H1573, MIA PaCa-2, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.81×** | +4.5 | 3e-04 | 12/37 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +4.4 | 5e-04 | 12/37 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.2 | 0.001 | 11/34 (RPMI-7951, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +4.1 | 0.002 | 11/39 (A549, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.029 | 7/39 (A549, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.036 | 12/38 (J82, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13087.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.600×** | -7.1 | 6e-10 | 12/21 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.724×** | -6.6 | 1e-08 | 22/40 (A-427, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.747×** | -4.2 | 0.004 | 14/31 (A-427, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.781×** | -3.6 | 0.048 | 8/39 (A498, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.807×** | -3.5 | 0.048 | 11/40 (SHP-77, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.791×** | -3.4 | 0.063 | 8/39 (A549, SNU-423, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **0.794×** | -3.4 | 0.063 | 7/40 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | **0.797×** | -3.3 | 0.063 | 8/39 (HEC-1-A, COLO 205, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.649×** | -3.3 | 0.063 | 9/36 (C-33 A, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.799×** | -3.3 | 0.063 | 6/40 (NCI-H661, LS 180, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | 0.811× | -3.0 | 0.12 | 10/40 (hTERT-HPNE, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | 0.806× | -3.0 | 0.12 | 12/39 (COLO 205, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13087. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 21.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -13.3) |
| [[J82 (line)]] | alt | 14.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 29.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -14.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -8.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 9.89 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.5 µM 0.0938× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.336× (z -8.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 7.70 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.126× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0689× (z -8.8) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 17.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -8.7) |
| [[SHP-77 (line)]] | alt | 35.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.3) |
| [[SW1417 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -9.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.957 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 15.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13087), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF692]] | +0.67 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[CDK5RAP1]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[SNU13]] | +0.65 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[CKLF]] | +0.65 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[MMS19]] | +0.64 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[ASB13]] | +0.64 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[SMIM13]] | +0.64 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[MFSD14CP]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[TTLL4]] | +0.62 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TOMM5]] | +0.61 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[NCK1]] | +0.61 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[TRIM35]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED29]] | -0.63 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[USP11]] | -0.63 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.62 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[COQ7]] | -0.61 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[FAM120AOS]] | -0.61 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[CREBBP]] | -0.61 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[ABCA10]] | -0.61 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[TRIP12]] | -0.59 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[AKT1S1]] | -0.59 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[UBE2A]] | -0.58 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[CFAP70]] | -0.58 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[AP5S1]] | -0.58 | -0.61 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CUZD1]] | C | CUZD1 activity raises FAM24B's level | lines that do not express CUZD1 (9) vs lines expressing it (41) | 5.12× lower at baseline in the lines without CUZD1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: FAM24B, C10orf88B; co-absent with the target |
| [[GARIN1B]] | C | GARIN1B activity lowers FAM24B's level | lines that do not express GARIN1B (4) vs lines expressing it (46) | 2.26× higher at baseline in the lines without GARIN1B | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PGGHG, ALPK1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CUZD1]] | C | FAM24B activity raises CUZD1's level | lines that do not express FAM24B (8) vs lines expressing it (42) | 2.58× lower at baseline in the lines without FAM24B | 0.019 | ⚠ within organs, on part of the lines; also absent: CUZD1, C10orf88B; co-absent with the target |

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.633). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-0.7, -19.1); signed map (-38.2, -18.6). **Vector** length 75.0, 15.5% of its response variance represented; |z| ≥ 3 in 738 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +4.3 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +5.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +8.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +4.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +4.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.1 | -3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.0 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.9 | -3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.5 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 24 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:122,849,078-122,879,641 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC45962, AC073585.2 |
| Matched by | ensembl_id |

UniProt [Q8N5W8](https://www.uniprot.org/uniprotkb/Q8N5W8) carries no function annotation.

**Summary**, from NCBI Gene [196792](https://www.ncbi.nlm.nih.gov/gene/196792):

> Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23475](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23475) · Entrez [196792](https://www.ncbi.nlm.nih.gov/gene/196792) · UniProt [Q8N5W8](https://www.uniprot.org/uniprotkb/Q8N5W8) · Ensembl [ENSG00000213185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213185)

## Data

Gene col 13087: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13087); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13087, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13087]; `tensor/DDL_lfc|DDL_z.npy` [13087]; `embed/gene_vectors.npy` [13087]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13087 or target_col == 13087). Every well: [[FAM24B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM24B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
