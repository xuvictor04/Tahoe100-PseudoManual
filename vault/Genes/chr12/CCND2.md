---
symbol: "CCND2"
type: "gene"
col: 4032
ensembl_id: "ENSG00000118971"
name: "cyclin D2"
location: "12p13.32"
module: 118
arm: "-"
pooled_cpm: 34.08
n_lines_expressing: 13
n_dd_up: 34
n_dd_down: 8
n_dd_up_clean: 22
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# CCND2

*cyclin D2* — 12p13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (12 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.38× (z +20.5, q 0e+00, up in 6 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Erlotinib (drug)]] 0.05 µM: 0.632× (z -5.1, q 2e-04, down in 0 of 11 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXB9]] (+0.52, fdr 5e-05), [[POLR3G]] (+0.50, fdr 3e-05), [[TFRC]] (+0.47, fdr 5e-05); moves opposite to [[KAT6B]] (-0.51, fdr 4e-05), [[DNAJC30]] (-0.49, fdr 4e-05), [[ZNF446]] (-0.48, fdr 9e-05).
> It sits in the **-** arm of [[Module 118]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ACSS1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[GNPNAT1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4032.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.38×** | +20.5 | 0e+00 | 6/11 (A-427, C-33 A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.77×** | +15.8 | 0e+00 | 6/11 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.78×** | +15.3 | 0e+00 | 6/8 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.59×** | +11.3 | 1e-27 | 5/11 (A-427, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +10.0 | 1e-21 | 4/10 (Panc 03.27, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +6.9 | 5e-10 | 5/11 (A-427, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +5.1 | 3e-05 | 1/11 (A-427) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.52×** | +5.0 | 5e-05 | 3/11 (Panc 03.27, HS-578T, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.8 | 9e-05 | 1/11 (SW480) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.8 | 9e-05 | 5/11 (NCI-H23, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.48×** | +4.7 | 2e-04 | 0/11 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.5 | 3e-04 | 0/11 | top dose only | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +4.5 | 3e-04 | 10/11 (A-427, NCI-H23, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.67×** | +4.4 | 5e-04 | 1/11 (SW480) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.44×** | +4.3 | 6e-04 | 6/11 (Panc 03.27, SW48, …) | rises with dose | composition shift |
| [[venetoclax (drug)]] 5 µM |  | **1.78×** | +3.6 | 0.011 | 2/11 (SW480, H4) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.31×** | +3.2 | 0.039 | 4/11 (A-427, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.039 | 6/11 (LoVo, SW48, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.043 | 4/11 (A-427, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +3.0 | 0.056 | 0/11 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.062 | 4/11 (SW480, LoVo, …) | two highest doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.61×** | +3.0 | 0.063 | 5/11 (SW48, LoVo, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4032.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | **0.632×** | -5.1 | 2e-04 | 0/11 | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.708×** | -4.1 | 0.011 | 1/11 (HS-578T) | all doses, flat | position effect removed |
| [[Sulfisoxazole (drug)]] 0.5 µM |  | **0.736×** | -3.6 | 0.051 | 10/11 (H4, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.580×** | -3.4 | 0.077 | 2/11 (LoVo, HS-578T) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.582×** | -3.4 | 0.077 | 0/11 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 5 µM |  | **0.584×** | -3.3 | 0.077 | 0/11 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.752×** | -3.2 | 0.098 | 1/11 (HepG2/C3A) | inconsistent across doses |  |
| [[Hexylresorcinol (drug)]] 5 µM |  | **0.827×** | -3.2 | 0.098 | 10/11 (LoVo, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.831× | -3.1 | 0.10 | 0/11 | all doses, flat | position effect removed |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.770× | -3.1 | 0.10 | 0/11 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4032. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 28.7 | 4 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 6.47× (z +15.9) | — |
| [[LoVo (line)]] | wt | 295 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.379× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 135 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +11.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 405 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.244× (z -14.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.287× (z -13.0) |
| [[RKO (line)]] | wt | 232 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.323× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.22 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.35 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 196 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.91 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.32 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.50 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.35 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.72 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.93 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.21 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.39 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.93 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.33 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 5.19 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 187 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 41.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4032), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXB9]] | +0.52 | +0.39 / +0.45 | both halves | 5e-05 |  |
| [[POLR3G]] | +0.50 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[TFRC]] | +0.47 | +0.39 / +0.40 | both halves | 5e-05 |  |
| [[GNPNAT1]] | +0.47 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[PPARGC1B]] | +0.47 | +0.48 / +0.34 | both halves | 1e-04 |  |
| [[UGT8]] | +0.46 | +0.47 / +0.32 | both halves | 1e-04 |  |
| [[TMEM64]] | +0.46 | +0.45 / +0.33 | both halves | 1e-04 |  |
| [[SLC38A5]] | +0.45 | +0.53 / +0.33 | both halves | 1e-04 |  |
| [[SLC16A1]] | +0.45 | +0.49 / +0.35 | both halves | 1e-04 |  |
| [[TXLNGY-1]] | +0.45 | +0.47 / +0.37 | both halves | 9e-05 |  |
| [[BCAT1]] | +0.45 | +0.21 / +0.53 | both halves | 7e-04 | pathway: HALLMARK_ALLOGRAFT_REJECTION |
| [[PYCR1]] | +0.44 | +0.38 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KAT6B]] | -0.51 | -0.40 / -0.41 | both halves | 4e-05 |  |
| [[DNAJC30]] | -0.49 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[ZNF446]] | -0.48 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[CWF19L2]] | -0.47 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[WDR83OS]] ⚠ | -0.47 | -0.37 / -0.44 | both halves | 9e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF324]] | -0.46 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[ZER1]] | -0.45 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[GPATCH8]] | -0.45 | -0.37 / -0.40 | both halves | 9e-05 |  |
| [[RTF1]] | -0.44 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[RETREG3]] | -0.44 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[IFT43]] | -0.43 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[KBTBD4]] | -0.43 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[ZBTB3]] | -0.43 | -0.37 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACSS1]] | B | ACSS1 activity lowers CCND2's level | lines that do not express ACSS1 (8) vs lines expressing it (42) | 2.40× higher at baseline in the lines without ACSS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PRXL2A, STAT5A, MGST2; maybe low, not absent; its own permutation p |
| [[SLC6A15]] | C | SLC6A15 activity raises CCND2's level | lines that do not express SLC6A15 (32) vs lines expressing it (18) | 1.33× lower at baseline in the lines without SLC6A15 | 0.085 | ⚠ within organs, on part of the lines; also absent: PAX3, CNKSR2, ENSG00000286251; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNPNAT1]] | B | CCND2 activity raises GNPNAT1's level | lines that do not express CCND2 (37) vs lines expressing it (13) | 1.47× lower at baseline in the lines without CCND2 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GPR15, MTND1P23, ENSG00000237031 |

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **-** arm (projection on the module's main direction -0.534). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-48.7, 10.7); signed map (-8.6, -56.2). **Vector** length 31.7, 7.37% of its response variance represented; |z| ≥ 3 in 334 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +20.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +15.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +15.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.1 | +3.6 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.9 | -3.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.8 | +2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | cyclin D2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.32 — chr12:4,269,771-4,305,353 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cyclins |
| Hallmark sets | ANGIOGENESIS, WNT_BETA_CATENIN_SIGNALING, ALLOGRAFT_REJECTION, APOPTOSIS, KRAS_SIGNALING_UP, IL2_STAT5_SIGNALING, P53_PATHWAY |
| Reactome | 12 pathways, smallest: Drug-mediated inhibition of CDK4/CDK6 activity; Aberrant regulation of mitotic G1/S transition in cancer due to RB1 defects; Defective binding of RB1 mutants to E2F1,(E2F2, E2F3) |
| Matched by | ensembl_id |

**Function**, from UniProt [P30279](https://www.uniprot.org/uniprotkb/P30279) (G1/S-specific cyclin-D2):

> Regulatory component of the cyclin D2-CDK4 (DC) complex that phosphorylates and inhibits members of the retinoblastoma (RB) protein family including RB1 and regulates the cell-cycle during G(1)/S transition. Phosphorylation of RB1 allows dissociation of the transcription factor E2F from the RB/E2F complex and the subsequent transcription of E2F target genes which are responsible for the progression through the G(1) phase. Hypophosphorylates RB1 in early G(1) phase. Cyclin D-CDK4 complexes are …

**Summary**, from NCBI Gene [894](https://www.ncbi.nlm.nih.gov/gene/894):

> The protein encoded by this gene belongs to the highly conserved cyclin family, whose members are characterized by a dramatic periodicity in protein abundance through the cell cycle. Cyclins function as regulators of CDK kinases. Different cyclins exhibit distinct expression and degradation patterns which contribute to the temporal coordination of each mitotic event. This cyclin forms a complex with CDK4 or CDK6 and functions as a regulatory subunit of the complex, whose activity is required …

**Accessions** — [HGNC:1583](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1583) · Entrez [894](https://www.ncbi.nlm.nih.gov/gene/894) · UniProt [P30279](https://www.uniprot.org/uniprotkb/P30279) · Ensembl [ENSG00000118971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118971)

## Data

Gene col 4032: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4032); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4032, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4032]; `tensor/DDL_lfc|DDL_z.npy` [4032]; `embed/gene_vectors.npy` [4032]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4032 or target_col == 4032). Every well: [[CCND2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCND2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
