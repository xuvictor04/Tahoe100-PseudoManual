---
symbol: "AK9"
type: "gene"
col: 7866
ensembl_id: "ENSG00000155085"
name: "adenylate kinase 9"
location: "6q21"
module: 10
arm: "+"
pooled_cpm: 11.55
n_lines_expressing: 49
n_dd_up: 37
n_dd_down: 15
n_dd_up_clean: 30
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# AK9

*adenylate kinase 9* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.85× (z +21.9, q 0e+00, up in 39 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.579× (z -6.3, q 2e-07, down in 28 of 45 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAH12]] (+0.83, fdr 7e-06), [[LINC02340]] (+0.82, fdr 7e-06), [[TMEM202-AS1]] (+0.82, fdr 1e-05); moves opposite to [[GNA12]] (-0.69, fdr 1e-04), [[CPSF4]] (-0.68, fdr 9e-06), [[L2HGDH]] (-0.68, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FSIP2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7866.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.85×** | +21.9 | 0e+00 | 39/42 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.75×** | +21.5 | 0e+00 | 41/42 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.52×** | +14.5 | 3e-45 | 38/42 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.94×** | +10.7 | 9e-25 | 39/46 (HS-578T, HEC-1-A, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +9.2 | 6e-18 | 35/43 (HS-578T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +7.9 | 2e-13 | 34/44 (SW480, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.77×** | +6.6 | 4e-09 | 31/46 (KATO III, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.75×** | +6.4 | 9e-09 | 33/45 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +6.1 | 6e-08 | 26/44 (SK-MEL-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.67×** | +5.9 | 2e-07 | 29/46 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.66×** | +5.8 | 3e-07 | 21/45 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +5.6 | 1e-06 | 26/46 (NCI-H2347, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +5.4 | 3e-06 | 23/45 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +5.4 | 3e-06 | 21/37 (NCI-H460, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.36×** | +4.9 | 3e-05 | 22/47 (LS 180, HT-29, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +4.8 | 5e-05 | 21/45 (HS-578T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.35×** | +4.8 | 7e-05 | 15/46 (SW480, SW48, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7866.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.579×** | -6.3 | 2e-07 | 28/45 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.594×** | -6.0 | 6e-07 | 23/46 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.599×** | -5.9 | 7e-07 | 26/45 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.430×** | -5.1 | 5e-05 | 24/43 (COLO 205, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.694×** | -4.2 | 0.003 | 23/46 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.697×** | -4.0 | 0.006 | 20/40 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.712×** | -3.9 | 0.008 | 18/47 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.556×** | -3.5 | 0.028 | 13/32 (HCT15, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.727×** | -3.5 | 0.032 | 12/45 (Hs 766T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.744×** | -3.4 | 0.036 | 17/45 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.681×** | -3.2 | 0.079 | 9/46 (HEC-1-A, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | **0.764×** | -3.1 | 0.088 | 10/45 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.766×** | -3.1 | 0.090 | 12/46 (SW480, LS 180, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.606×** | -3.0 | 0.099 | 11/45 (COLO 205, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.607×** | -3.0 | 0.099 | 9/42 (SHP-77, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7866. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 7.59 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +14.4) | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -10.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 5.67 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +10.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0675× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[NCI-H1792 (line)]] | alt | 14.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 5.65 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.2× (z +17.2) | — |
| [[NCI-H460 (line)]] | wt | 8.95 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +14.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.186× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 11.8 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +11.9) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.156× (z -12.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SK-MEL-2 (line)]] | alt | 24.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.80× (z +16.2) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -8.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 14.5 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +13.4) | [[Digitoxin (drug)]] 0.5 µM 0.234× (z -10.4) |
| [[A498 (line)]] | wt | 3.18 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +8.6) | [[Monocrotaline (drug)]] 0.05 µM 0.0721× (z -8.8) |
| [[BT-474 (line)]] | alt | 10.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +9.1) | [[Pimozide (drug)]] 0.5 µM 0.0952× (z -9.1) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 16.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +8.8) | — |
| [[C32 (line)]] | wt | 13.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +10.4) | — |
| [[HCT15 (line)]] | alt | 18.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.98× (z +13.7) | — |
| [[HEC-1-A (line)]] | alt | 20.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.69× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -11.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 20.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +10.3) | — |
| [[LoVo (line)]] | wt | 11.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +13.9) | — |
| [[LOX-IMVI (line)]] | wt | 6.82 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.63× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 23.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +11.1) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.138× (z -11.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H23 (line)]] | alt | 7.08 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.35× (z +11.5) | [[Digitoxin (drug)]] 5 µM 0.109× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[NCI-H2347 (line)]] | alt | 7.11 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.56× (z +12.5) | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.31× (z +10.5) | [[Ixazomib citrate (drug)]] 5 µM 0.143× (z -8.7) |
| [[A-172 (line)]] | wt | 10.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.47× (z +12.2) | — |
| [[CFPAC-1 (line)]] | alt | 7.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +9.5) | — |
| [[HepG2_C3A (line)]] | wt | 24.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 4.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.98× (z +9.7) | — |
| [[J82 (line)]] | alt | 9.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 5.87 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 20.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 22.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +9.1) | — |
| [[SW 900 (line)]] | alt | 12.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +9.0) | — |
| [[A-427 (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7866), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAH12]] | +0.83 | +0.86 / +0.71 | both halves | 7e-06 |  |
| [[LINC02340]] | +0.82 | +0.88 / +0.69 | both halves | 7e-06 |  |
| [[TMEM202-AS1]] | +0.82 | +0.84 / +0.54 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.81 | +0.88 / +0.47 | both halves | 2e-05 |  |
| [[THAP2]] | +0.81 | +0.86 / +0.50 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.81 | +0.85 / +0.60 | both halves | 7e-06 |  |
| [[N4BP2L1]] | +0.80 | +0.83 / +0.62 | both halves | 7e-06 |  |
| [[CCDC90B-AS1]] | +0.79 | +0.84 / +0.46 | both halves | 3e-05 |  |
| [[KRCC1]] | +0.79 | +0.83 / +0.51 | both halves | 1e-05 |  |
| [[METTL6]] | +0.78 | +0.85 / +0.46 | both halves | 3e-05 |  |
| [[UFL1-AS1]] | +0.78 | +0.79 / +0.57 | both halves | 9e-06 |  |
| [[PDCL3P4]] | +0.78 | +0.86 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNA12]] | -0.69 | -0.73 / -0.33 | both halves | 1e-04 |  |
| [[CPSF4]] | -0.68 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[L2HGDH]] | -0.68 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[GTF2E2]] | -0.68 | -0.66 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises AK9's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.80× lower at baseline in the lines without FSIP2-AS1 | 0.026 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[LINC00504]] | B | LINC00504 activity raises AK9's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 1.57× lower at baseline in the lines without LINC00504 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474 |
| [[TOP2A]] | B | TOP2A activity lowers AK9's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC02147]] | B | LINC02147 activity raises AK9's level | lines that do not express LINC02147 (26) vs lines expressing it (24) | 1.73× lower at baseline in the lines without LINC02147 | 0.092 | ⚠ within organs, on part of the lines; also absent: LINC00992, PROX1-AS1, MOGAT3; maybe low, not absent |
| [[UBA6-DT]] | C | UBA6-DT activity raises AK9's level | lines that do not express UBA6-DT (3) vs lines expressing it (47) | 2.10× lower at baseline in the lines without UBA6-DT | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ZNF419, C2orf27A, CLEC2D; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.762). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.2, 14.4); signed map (27.0, -10.4). **Vector** length 88.8, 20.2% of its response variance represented; |z| ≥ 3 in 1,096 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.7 | +14.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.7 | +21.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +21.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +10.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +5.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.2 | +4.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -5.2 | +2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.8 | +5.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.3 | +5.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | -0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.0 | -5.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | +3.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -3.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | adenylate kinase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:109,492,855-109,691,217 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ42177, FLJ25791, dJ70A9.1, MGC26954; previously C6orf224, AKD2, C6orf199, AKD1 |
| Gene groups (HGNC) | Adenylate kinases |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TCS8](https://www.uniprot.org/uniprotkb/Q5TCS8) (Adenylate kinase 9):

> Broad-specificity nucleoside phosphate kinase involved in cellular nucleotide homeostasis by catalyzing nucleoside-phosphate interconversions. Similar to other adenylate kinases, preferentially catalyzes the phosphorylation of the nucleoside monophosphate AMP with ATP as phosphate donor to produce ADP. In vitro, can also catalyze the phosphorylation of CMP, dAMP and dCMP and use GTP as an alternate phosphate donor. Moreover, exhibits a diphosphate kinase activity, producing ATP, CTP, GTP, UTP, …

**Summary**, from NCBI Gene [221264](https://www.ncbi.nlm.nih.gov/gene/221264):

> The protein encoded by this gene catalyzes the interconversion of nucleosides, possessing both nucleoside monophosphate and diphosphate kinase activities. The encoded protein uses these interconversions to maintain nucleoside homeostasis. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:33814](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33814) · Entrez [221264](https://www.ncbi.nlm.nih.gov/gene/221264) · UniProt [Q5TCS8](https://www.uniprot.org/uniprotkb/Q5TCS8) · Ensembl [ENSG00000155085](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155085)

## Data

Gene col 7866: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7866); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7866, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7866]; `tensor/DDL_lfc|DDL_z.npy` [7866]; `embed/gene_vectors.npy` [7866]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7866 or target_col == 7866). Every well: [[AK9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AK9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
