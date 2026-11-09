---
symbol: "PEBP1"
type: "gene"
col: 1578
ensembl_id: "ENSG00000089220"
name: "phosphatidylethanolamine binding protein 1"
location: "12q24.23"
module: 182
arm: "+"
pooled_cpm: 56.4
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# PEBP1

*phosphatidylethanolamine binding protein 1* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.41× (z +13.9, q 2e-41, up in 46 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +4.8, q 2e-04, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.609× (z -6.3, q 2e-07, down in 32 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IARS2]] (+0.69, fdr 7e-06), [[FAM210B]] (+0.65, fdr 1e-05), [[ASAH1]] (+0.65, fdr 7e-06); moves opposite to [[TUT7]] (-0.65, fdr 1e-05), [[ZNF562]] (-0.60, fdr 1e-05), [[LCAT]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 182]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC01589]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1578.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.41×** | +13.9 | 2e-41 | 46/46 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.84×** | +13.3 | 8e-38 | 38/39 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.53×** | +10.5 | 2e-23 | 42/44 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.71×** | +4.8 | 2e-04 | 41/47 (HOP62, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.8 | 2e-04 | 33/47 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +4.2 | 0.002 | 29/48 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +4.0 | 0.005 | 30/46 (HepG2/C3A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.60×** | +4.0 | 0.005 | 30/46 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | **1.54×** | +3.6 | 0.019 | 35/47 (A498, SNU-423, …) | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.4 | 0.034 | 23/35 (A-172, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.038 | 29/47 (SK-MEL-2, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1578.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.609×** | -6.3 | 2e-07 | 32/47 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.655×** | -3.8 | 0.039 | 33/47 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.477×** | -3.5 | 0.094 | 34/47 (HEC-1-A, SHP-77, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1578. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 55.0 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.69× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -8.9) |
| [[A-172 (line)]] | wt | 84.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +8.8) | — |
| [[A-427 (line)]] | wt | 64.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.14× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.0523× (z -19.6) |
| [[A549 (line)]] | wt | 45.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.59× (z +13.6) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 31.5 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.60× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 128 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +10.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 53.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.69× (z +13.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 46.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.54× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 45.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.94× (z +11.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 90.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -8.9) |
| [[KATO III (line)]] | alt | 54.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.07× (z +12.7) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 47.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 10.3× (z +14.8) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 73.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.25× (z +13.1) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 77.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.77× (z +12.2) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 33.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.5× (z +13.7) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 44.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.47× (z +13.8) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 54.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.85× (z +12.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 41.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +10.7) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 42.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.37× (z +9.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 83.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.34× (z +11.8) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 70.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.43× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 94.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +11.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 90.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.79× (z +12.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 21.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 19.9× (z +14.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 46.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 32.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.32× (z +10.1) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 73.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 70.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.40× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 71.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +11.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 75.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.86× (z +8.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 79.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 57.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +9.4) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 57.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +9.5) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 44.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.89× (z +9.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 64.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +10.0) | — |
| [[RKO (line)]] | wt | 82.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 48.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.59× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 30.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.12× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 37.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.71× (z +10.9) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 60.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.47 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 82.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1578), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IARS2]] | +0.69 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[FAM210B]] | +0.65 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[ASAH1]] | +0.65 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[KDM1A]] | +0.63 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[PCYOX1]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[RCN2]] | +0.61 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[RPS3A]] | +0.59 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[HNRNPA1]] | +0.59 | +0.69 / +0.44 | both halves | 3e-05 |  |
| [[RPL22]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[SNX4]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SNRPA1]] | +0.57 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[RPS2]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 | STRING 591 |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUT7]] | -0.65 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[ZNF562]] | -0.60 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[LCAT]] | -0.60 | -0.57 / -0.43 | both halves | 4e-05 |  |
| [[FAM83G]] | -0.59 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[SSUH2]] | -0.58 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.58 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[SETX]] | -0.58 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[EXOC8]] | -0.58 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[TNFRSF12A]] | -0.57 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[KHNYN]] | -0.57 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[ZNF274]] | -0.55 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[THAP5]] | -0.55 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01589]] | B | LINC01589 activity lowers PEBP1's level | lines that do not express LINC01589 (23) vs lines expressing it (27) | 1.41× higher at baseline in the lines without LINC01589 | 0.066 | ⚠ within organs, on part of the lines; also absent: HNF1B, ENSG00000279806, GOLT1A |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **+** arm (projection on the module's main direction 0.700). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-18.4, -18.8); signed map (-51.6, -8.8). **Vector** length 67.8, 21.6% of its response variance represented; |z| ≥ 3 in 637 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.4 | +3.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | +1.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | -1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.8 | -1.3 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.8 | +0.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | +1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -6.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | +0.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -0.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.8 | +1.2 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylethanolamine binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.23 — chr12:118,136,124-118,145,584 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RKIP, HCNP, PEBP; previously PBP |
| Hallmark sets | SPERMATOGENESIS |
| Reactome | 13 pathways, smallest: Signaling by high-kinase activity BRAF mutants; MAP2K and MAPK activation; Negative regulation of MAPK pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P30086](https://www.uniprot.org/uniprotkb/P30086) (Phosphatidylethanolamine-binding protein 1):

> Binds ATP, opioids and phosphatidylethanolamine. Has lower affinity for phosphatidylinositol and phosphatidylcholine. Serine protease inhibitor which inhibits thrombin, neuropsin and chymotrypsin but not trypsin, tissue type plasminogen activator and elastase (By similarity). Inhibits the kinase activity of RAF1 by inhibiting its activation and by dissociating the RAF1/MEK complex and acting as a competitive inhibitor of MEK phosphorylation.; HCNP may be involved in the function of the …

**Summary**, from NCBI Gene [5037](https://www.ncbi.nlm.nih.gov/gene/5037):

> This gene encodes a member of the phosphatidylethanolamine-binding family of proteins and has been shown to modulate multiple signaling pathways, including the MAP kinase (MAPK), NF-kappa B, and glycogen synthase kinase-3 (GSK-3) signaling pathways. The encoded protein can be further processed to form a smaller cleavage product, hippocampal cholinergic neurostimulating peptide (HCNP), which may be involved in neural development. This gene has been implicated in numerous human cancers and may …

**Accessions** — [HGNC:8630](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8630) · Entrez [5037](https://www.ncbi.nlm.nih.gov/gene/5037) · UniProt [P30086](https://www.uniprot.org/uniprotkb/P30086) · Ensembl [ENSG00000089220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089220)

## Data

Gene col 1578: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1578); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1578, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1578]; `tensor/DDL_lfc|DDL_z.npy` [1578]; `embed/gene_vectors.npy` [1578]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1578 or target_col == 1578). Every well: [[PEBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
