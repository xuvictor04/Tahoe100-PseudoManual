---
symbol: "PRR5L"
type: "gene"
col: 5689
ensembl_id: "ENSG00000135362"
name: "proline rich 5 like"
location: "11p13-p12"
module: 5
arm: "+"
pooled_cpm: 30.0
n_lines_expressing: 40
n_dd_up: 7
n_dd_down: 23
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PRR5L

*proline rich 5 like* — 11p13-p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.05 µM: 1.43× (z +4.5, q 0.003, up in 16 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.219× (z -27.0, q 0e+00, down in 33 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRG]] (+0.63, fdr 1e-05), [[LARP4B]] (+0.59, fdr 3e-05), [[STXBP5-AS1]] (+0.57, fdr 3e-05); moves opposite to [[C15orf48]] (-0.50, fdr 4e-05), [[SVIP]] (-0.50, fdr 9e-05), [[DDAH2]] (-0.50, fdr 5e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STARD10]] → it (grade C ⚠); 4 go from it, the strongest it → [[FAM120A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5689.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +4.5 | 0.003 | 16/36 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.42×** | +4.4 | 0.003 | 15/36 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.41×** | +4.3 | 0.003 | 16/38 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.39×** | +3.8 | 0.023 | 17/36 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.057 | 16/38 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.057 | 12/38 (HOP62, HS-578T, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.086 | 17/38 (HOP62, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5689.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.219×** | -27.0 | 0e+00 | 33/37 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.276×** | -15.6 | 0e+00 | 35/37 (RKO, SW1417, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.327×** | -14.1 | 1e-42 | 33/38 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.374×** | -12.4 | 4e-33 | 31/38 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.414×** | -11.1 | 1e-26 | 25/36 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.425×** | -10.8 | 4e-25 | 33/38 (HT-29, SNU-423, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.435×** | -10.5 | 8e-24 | 28/37 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.520×** | -8.3 | 1e-14 | 26/38 (LoVo, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.671×** | -5.0 | 3e-05 | 18/36 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.681×** | -4.7 | 2e-04 | 21/35 (HCT15, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.710×** | -4.3 | 8e-04 | 20/38 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.703×** | -4.3 | 9e-04 | 21/34 (C32, SW48, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.792×** | -4.2 | 0.001 | 17/38 (J82, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.725×** | -4.1 | 0.002 | 13/37 (C32, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.728×** | -4.0 | 0.002 | 17/35 (HT-29, J82, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.750×** | -3.5 | 0.013 | 17/38 (A-172, LoVo, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.843× | -3.1 | 0.058 | 8/38 (NCI-H460, COLO 205, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.786×** | -3.1 | 0.058 | 14/38 (SW48, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5689. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 58.7 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -18.4) |
| [[HT-29 (line)]] | alt | 226 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0479× (z -25.8) |
| [[COLO 205 (line)]] | alt | 61.4 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0782× (z -24.8) |
| [[LoVo (line)]] | wt | 45.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -16.5) |
| [[NCI-H460 (line)]] | wt | 81.3 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0898× (z -19.5) |
| [[A-172 (line)]] | wt | 45.1 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0745× (z -28.8) |
| [[SW1417 (line)]] | alt | 53.7 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0600× (z -25.9) |
| [[SW480 (line)]] | alt | 24.6 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -19.2) |
| [[LS 180 (line)]] | wt | 50.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -21.7) |
| [[SNU-423 (line)]] | alt | 52.1 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0923× (z -21.6) |
| [[J82 (line)]] | alt | 60.0 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 23.4 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.172× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 25.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -19.2) |
| [[HOP62 (line)]] | alt | 29.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -13.9) |
| [[RKO (line)]] | wt | 19.8 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0392× (z -17.9) |
| [[A549 (line)]] | wt | 18.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -16.4) |
| [[HCT15 (line)]] | alt | 22.2 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0634× (z -12.6) ⚠ toxic; cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.250× (z -9.3) |
| [[HS-578T (line)]] | alt | 29.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -15.9) |
| [[hTERT-HPNE (line)]] | wt | 25.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -14.1) |
| [[PANC-1 (line)]] | alt | 8.93 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -12.8) |
| [[RPMI-7951 (line)]] | alt | 27.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.148× (z -10.3) |
| [[SW48 (line)]] | wt | 20.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -12.3) |
| [[A498 (line)]] | wt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -16.7) |
| [[AsPC-1 (line)]] | alt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -9.6) |
| [[C-33 A (line)]] | alt | 21.5 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.141× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0969× (z -15.7) |
| [[H4 (line)]] | wt | 39.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 25.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.122× (z -13.6) |
| [[SNU-1 (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0943× (z -10.0) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 28.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0733× (z -8.8) |
| [[A-427 (line)]] | wt | 5.17 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.97 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.85 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.34 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.49 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5689), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRG]] | +0.63 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[LARP4B]] | +0.59 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[STXBP5-AS1]] | +0.57 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[SIRPA]] | +0.56 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[TSR1]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[TBXAS1]] | +0.54 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[TLCD3A]] | +0.53 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[RBM19]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[LARP4]] | +0.52 | +0.41 / +0.37 | both halves | 8e-05 |  |
| [[DIAPH2]] | +0.51 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[RAP1GDS1]] | +0.50 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[FRMD3]] | +0.50 | +0.47 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C15orf48]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[SVIP]] | -0.50 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[DDAH2]] | -0.50 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[ATG4D]] | -0.49 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[CRTC1]] | -0.48 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[RBM4B]] | -0.48 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[MIEN1]] | -0.48 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[SIGIRR]] | -0.47 | -0.28 / -0.36 | both halves | 3e-04 |  |
| [[PRMT9]] | -0.47 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[PGPEP1]] | -0.47 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[MOSPD2]] | -0.46 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[FAM229B]] | -0.46 | -0.29 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD10]] | C | STARD10 activity lowers PRR5L's level | lines that do not express STARD10 (4) vs lines expressing it (46) | 2.11× higher at baseline in the lines without STARD10 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CARD10, DNM1, SDC1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM120A]] | B | PRR5L activity raises FAM120A's level | lines that do not express PRR5L (10) vs lines expressing it (40) | 1.43× lower at baseline in the lines without PRR5L | 0.051 | ⚠ within organs, on part of the lines; also absent: RASA3, DUSP5-DT, HOXA13; maybe low, not absent |
| [[EIF4G1]] | B | PRR5L activity lowers EIF4G1's level | lines that do not express PRR5L (10) vs lines expressing it (40) | 1.14× higher at baseline in the lines without PRR5L | 0.053 | ⚠ within organs, on part of the lines; also absent: RASA3, DUSP5-DT, HOXA13; maybe low, not absent |
| [[L3HYPDH]] | B | PRR5L activity raises L3HYPDH's level | lines that do not express PRR5L (10) vs lines expressing it (40) | 1.38× lower at baseline in the lines without PRR5L | 0.063 | ⚠ within organs, on part of the lines; also absent: RASA3, DUSP5-DT, HOXA13; maybe low, not absent |
| [[LDLRAD3]] | B | PRR5L activity raises LDLRAD3's level | lines that do not express PRR5L (10) vs lines expressing it (40) | 2.81× lower at baseline in the lines without PRR5L | 0.076 | ⚠ within organs, on part of the lines; also absent: RASA3, DUSP5-DT, HOXA13; maybe low, not absent |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.510). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-14.2, 30.4); signed map (17.0, 23.4). **Vector** length 84.4, 19.3% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.7 | -1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.5 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +0.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.5 | +4.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.3 | +4.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.3 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -27.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.5 | -15.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.4 | -4.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.6 | -10.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.2 | -0.4 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -1.1 | +0.2 |
|  | [[Hexylresorcinol (drug)]] 5 µM |  | -1.1 | -0.5 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -1.0 | -1.6 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | proline rich 5 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13-p12 — chr11:36,296,288-36,465,204 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14213, PROTOR-2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6MZQ0](https://www.uniprot.org/uniprotkb/Q6MZQ0) (Proline-rich protein 5-like):

> Associates with the mTORC2 complex that regulates cellular processes including survival and organization of the cytoskeleton. Regulates the activity of the mTORC2 complex in a substrate-specific manner preventing for instance the specific phosphorylation of PKCs and thereby controlling cell migration. Plays a role in the stimulation of ZFP36-mediated mRNA decay of several ZFP36-associated mRNAs, such as TNF and GM-CSF, in response to stress. Required for ZFP36 localization to cytoplasmic stress …

**Summary**, from NCBI Gene [79899](https://www.ncbi.nlm.nih.gov/gene/79899):

> Enables ubiquitin protein ligase binding activity. Involved in several processes, including TORC2 signaling; positive regulation of intracellular protein transport; and regulation of fibroblast migration. Part of TORC2 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25878](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25878) · Entrez [79899](https://www.ncbi.nlm.nih.gov/gene/79899) · UniProt [Q6MZQ0](https://www.uniprot.org/uniprotkb/Q6MZQ0) · Ensembl [ENSG00000135362](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135362)

## Data

Gene col 5689: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5689); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5689, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5689]; `tensor/DDL_lfc|DDL_z.npy` [5689]; `embed/gene_vectors.npy` [5689]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5689 or target_col == 5689). Every well: [[PRR5L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRR5L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
