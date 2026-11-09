---
symbol: "CFAP300"
type: "gene"
col: 6047
ensembl_id: "ENSG00000137691"
name: "cilia and flagella associated protein 300"
location: "11q22.1"
module: 223
arm: "+"
pooled_cpm: 3.21
n_lines_expressing: 32
n_dd_up: 19
n_dd_down: 9
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/223"]
generated_by: "tahoemap"
---

# CFAP300

*cilia and flagella associated protein 300* — 11q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.48× (z +8.2, q 1e-13, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.66× (z +6.7, q 6e-09, up in 10 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.546× (z -5.7, q 8e-06, down in 15 of 26 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAP3K2-DT]] (+0.62, fdr 7e-06), [[ZFHX2]] (+0.60, fdr 1e-05), [[KLRC2]] (+0.60, fdr 2e-05); moves opposite to [[FBH1]] (-0.55, fdr 2e-05), [[ZCCHC17]] (-0.51, fdr 3e-05), [[DPP9]] (-0.49, fdr 1e-05).
> It is in [[Module 223]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CYP1B1]] → it (grade B ⚠); 5 go from it, the strongest it → [[FOSL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6047.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.48×** | +8.2 | 1e-13 | 3/6 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.66×** | +6.7 | 6e-09 | 10/28 (A-427, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +6.2 | 1e-07 | 4/13 (HS-578T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.83×** | +5.7 | 2e-06 | 12/23 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.51×** | +5.5 | 5e-06 | 11/27 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.86×** | +5.4 | 7e-06 | 2/8 (Hs 766T, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +4.6 | 4e-04 | 10/23 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +4.5 | 4e-04 | 3/14 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +4.4 | 8e-04 | 13/29 (PANC-1, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.59×** | +4.4 | 8e-04 | 9/27 (Hs 766T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.005 | 9/29 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +3.9 | 0.005 | 5/22 (PANC-1, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.31×** | +3.6 | 0.014 | 5/28 (A-172, A549, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.44×** | +3.4 | 0.027 | 2/24 (HS-578T, NCI-H23) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.043 | 3/28 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.053 | 6/27 (PANC-1, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +3.1 | 0.056 | 3/26 (PANC-1, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.081 | 3/25 (COLO 205, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6047.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.546×** | -5.7 | 8e-06 | 15/26 (RPMI-7951, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.616×** | -4.5 | 0.002 | 14/29 (PANC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.718×** | -4.4 | 0.002 | 11/26 (CFPAC-1, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.636×** | -4.2 | 0.003 | 13/25 (PANC-1, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.671×** | -3.7 | 0.018 | 14/28 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.671×** | -3.7 | 0.018 | 12/27 (NCI-H23, A-427, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.676×** | -3.7 | 0.021 | 9/28 (NCI-H460, NCI-H23, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.511×** | -3.3 | 0.072 | 8/17 (HS-578T, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.518×** | -3.2 | 0.081 | 7/22 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.703× | -3.1 | 0.11 | 10/24 (SW 900, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Aprepitant (drug)]] 0.05 µM |  | 0.720× | -3.1 | 0.11 | 3/25 (COLO 205, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6047. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 25.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0687× (z -9.8) |
| [[PANC-1 (line)]] | alt | 7.68 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.170× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 5.94 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0775× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 3.98 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.0720× (z -8.5) |
| [[A-172 (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.496 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.841 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.363 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.486 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.298 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.360 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.407 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.353 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.581 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.343 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.350 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.525 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6047), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP3K2-DT]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ZFHX2]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[KLRC2]] | +0.60 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[RPS6KA6]] | +0.59 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[KLRC3]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[LINC01569]] | +0.55 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[CXXC4]] | +0.55 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[LINC01273]] | +0.54 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[KLRC4-KLRK1]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[REL]] | +0.54 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[ZMAT1]] | +0.54 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[BCL3]] | +0.53 | +0.39 / +0.54 | both halves | 5e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBH1]] | -0.55 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ZCCHC17]] | -0.51 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[DPP9]] | -0.49 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[MFN1]] | -0.49 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[TMEM181]] | -0.48 | -0.29 / -0.53 | both halves | 2e-04 |  |
| [[TOP3A]] | -0.48 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[TMEM104]] | -0.48 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[PDCD6]] | -0.47 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[VPS53]] | -0.46 | -0.32 / -0.52 | both halves | 2e-04 |  |
| [[RECQL]] | -0.46 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[DNAJC5]] | -0.46 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[GDI2]] | -0.45 | -0.46 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP1B1]] | B | CYP1B1 activity raises CFAP300's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 2.13× lower at baseline in the lines without CYP1B1 | 0.060 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FOSL2]] | B | CFAP300 activity raises FOSL2's level | lines that do not express CFAP300 (18) vs lines expressing it (32) | 1.31× lower at baseline in the lines without CFAP300 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, ARID1A; also absent: MYPN, GATA3, CCL5 |
| [[TMEM181]] | B | CFAP300 activity lowers TMEM181's level | lines that do not express CFAP300 (18) vs lines expressing it (32) | 1.46× higher at baseline in the lines without CFAP300 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, ARID1A; also absent: MYPN, GATA3, CCL5 |
| [[ZNF630]] | B | CFAP300 activity raises ZNF630's level | lines that do not express CFAP300 (18) vs lines expressing it (32) | 2.65× lower at baseline in the lines without CFAP300 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, ARID1A; also absent: MYPN, GATA3, CCL5 |
| [[ZFHX2]] | B | CFAP300 activity lowers ZFHX2's level | lines that do not express CFAP300 (18) vs lines expressing it (32) | 1.25× higher at baseline in the lines without CFAP300 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, ARID1A; also absent: MYPN, GATA3, CCL5 |
| [[TOP3A]] | B | CFAP300 activity lowers TOP3A's level | lines that do not express CFAP300 (18) vs lines expressing it (32) | 1.11× higher at baseline in the lines without CFAP300 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with SETD1B, ARID1A; also absent: MYPN, GATA3, CCL5 |

## Where it sits

- **Module**: [[Module 223]]; 10 genes; every member is in the + arm (projection on the module's main direction 0.633). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.1, 8.1); signed map (50.7, 19.5). **Vector** length 38.9, 6.19% of its response variance represented; |z| ≥ 3 in 558 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +4.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.3 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.0 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +5.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +3.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +0.9 | +2.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.9 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -4.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -2.5 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.2 | -2.2 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.1 | -3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 300 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.1 — chr11:102,047,437-102,084,554 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC13040, FBB5, DNAAF17; previously C11orf70 |
| Gene groups (HGNC) | Cilia and flagella associated; Axonemal dynein assembly factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRQ4](https://www.uniprot.org/uniprotkb/Q9BRQ4) (Cilia- and flagella-associated protein 300):

> Cilium- and flagellum-specific protein that plays a role in axonemal structure organization and motility. May play a role in outer and inner dynein arm assembly.

**Summary**, from NCBI Gene [85016](https://www.ncbi.nlm.nih.gov/gene/85016):

> Predicted to be located in cytoplasm and motile cilium. Implicated in primary ciliary dyskinesia 38. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28188) · Entrez [85016](https://www.ncbi.nlm.nih.gov/gene/85016) · UniProt [Q9BRQ4](https://www.uniprot.org/uniprotkb/Q9BRQ4) · Ensembl [ENSG00000137691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137691)

## Data

Gene col 6047: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6047); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6047, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6047]; `tensor/DDL_lfc|DDL_z.npy` [6047]; `embed/gene_vectors.npy` [6047]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6047 or target_col == 6047). Every well: [[CFAP300 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP300.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
