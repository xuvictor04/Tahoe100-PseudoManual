---
symbol: "TPD52"
type: "gene"
col: 1154
ensembl_id: "ENSG00000076554"
name: "tumor protein D52"
location: "8q21.13"
module: 99
arm: "+"
pooled_cpm: 272.62
n_lines_expressing: 48
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# TPD52

*tumor protein D52* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.28× (z +5.2, q 1e-04, up in 30 of 46 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.18× (z +5.0, q 2e-04, up in 23 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.272× (z -37.7, q 0e+00, down in 46 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDON]] (+0.76, fdr 7e-06), [[PDK1]] (+0.75, fdr 7e-06), [[HK2]] (+0.75, fdr 7e-06); moves opposite to [[SPRY3]] (-0.66, fdr 3e-05), [[FIZ1]] (-0.65, fdr 7e-06), [[ERCC6L2]] (-0.64, fdr 4e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1154.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +5.2 | 1e-04 | 30/46 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +5.0 | 2e-04 | 23/46 (C32, HS-578T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.23×** | +4.4 | 0.002 | 24/47 (C32, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.14× | +3.9 | 0.016 | 8/46 (BT-474, SNU-1, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.016 | 28/46 (KATO III, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.20× | +3.6 | 0.027 | 15/47 (NCI-H460, HepG2/C3A, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.033 | 16/46 (NCI-H2030, Hs 766T, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.13× | +3.4 | 0.042 | 10/46 (SHP-77, SNU-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.044 | 25/47 (HOP62, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.058 | 24/46 (HEC-1-A, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.058 | 19/46 (CFPAC-1, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.074 | 20/46 (NCI-H460, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 5 µM |  | 1.17× | +3.1 | 0.078 | 13/47 (NCI-H2030, HEC-1-A, …) | top dose only | plate-row cell shift |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 1.16× | +3.1 | 0.088 | 11/46 (NCI-H2030, NCI-H460, …) | rises with dose | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1154.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.272×** | -37.7 | 0e+00 | 46/46 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.311×** | -24.6 | 0e+00 | 46/46 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.429×** | -24.5 | 0e+00 | 44/47 (C32, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.342×** | -21.8 | 0e+00 | 45/46 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.614×** | -14.4 | 6e-45 | 45/46 (A498, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.596×** | -10.5 | 1e-23 | 42/45 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.660×** | -8.8 | 2e-16 | 36/46 (LoVo, SHP-77, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.679×** | -7.9 | 3e-13 | 35/45 (C32, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.723×** | -6.8 | 5e-10 | 31/46 (SHP-77, LoVo, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.729×** | -6.4 | 9e-09 | 29/46 (C32, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.811×** | -6.1 | 5e-08 | 26/46 (NCI-H2347, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.755×** | -5.7 | 6e-07 | 31/48 (C32, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.765×** | -5.6 | 7e-07 | 28/46 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.770×** | -5.5 | 1e-06 | 31/46 (C32, NCI-H460, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.801×** | -4.7 | 1e-04 | 28/46 (Hs 766T, A-172, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.878× | -3.7 | 0.006 | 10/46 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.839× | -3.7 | 0.007 | 20/46 (NCI-H1573, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.839× | -3.7 | 0.007 | 21/46 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.859× | -3.2 | 0.037 | 11/47 (NCI-H2030, A549, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.864× | -3.1 | 0.051 | 14/47 (KATO III, Hs 766T, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.900× | -3.0 | 0.054 | 8/46 (A498, Hs 766T, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.902× | -3.0 | 0.056 | 6/46 (A498, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1154. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 551 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -41.7) |
| [[NCI-H460 (line)]] | wt | 306 | 1 | 10 (3 ⚠) | [[Gefitinib (drug)]] 5 µM 1.86× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -30.1) |
| [[BT-474 (line)]] | alt | 422 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -21.6) |
| [[NCI-H2347 (line)]] | alt | 374 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -33.6) |
| [[PANC-1 (line)]] | alt | 310 | 1 | 9 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 2.87× (z +9.8) | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -28.8) |
| [[C-33 A (line)]] | alt | 443 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -23.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.381× (z -17.9) |
| [[HepG2_C3A (line)]] | wt | 228 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -32.4) |
| [[A549 (line)]] | wt | 279 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -26.7) |
| [[LoVo (line)]] | wt | 346 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -42.2) |
| [[RKO (line)]] | wt | 407 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -26.9) |
| [[SHP-77 (line)]] | alt | 434 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -24.7) |
| [[A498 (line)]] | wt | 170 | 0 | 7 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.226× (z -22.5) |
| [[KATO III (line)]] | alt | 244 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -21.5) |
| [[LS 180 (line)]] | wt | 442 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -24.9) |
| [[SW480 (line)]] | alt | 194 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -24.4) |
| [[HEC-1-A (line)]] | alt | 346 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -19.3) |
| [[HOP62 (line)]] | alt | 194 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -15.1) |
| [[J82 (line)]] | alt | 433 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -19.3) |
| [[MIA PaCa-2 (line)]] | alt | 219 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -28.9) |
| [[SK-MEL-2 (line)]] | alt | 282 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -34.5) |
| [[SNU-423 (line)]] | alt | 176 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -17.2) |
| [[AsPC-1 (line)]] | alt | 202 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -24.8) |
| [[Hs 766T (line)]] | wt | 142 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -17.6) |
| [[HS-578T (line)]] | alt | 116 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -22.0) |
| [[HT-29 (line)]] | alt | 254 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -30.3) |
| [[NCI-H1573 (line)]] | alt | 528 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -35.2) |
| [[NCI-H23 (line)]] | alt | 134 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -30.2) |
| [[SNU-1 (line)]] | wt | 275 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -19.5) |
| [[SW1417 (line)]] | alt | 154 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -20.0) |
| [[A-172 (line)]] | wt | 147 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -21.9) |
| [[A-427 (line)]] | wt | 220 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.365× (z -17.4) |
| [[AN3 CA (line)]] | alt | 292 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.204× (z -11.6) |
| [[COLO 205 (line)]] | alt | 198 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -20.0) |
| [[NCI-H1792 (line)]] | alt | 218 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -28.6) |
| [[NCI-H2030 (line)]] | alt | 628 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -16.1) |
| [[Panc 03.27 (line)]] | alt | 175 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -21.8) |
| [[RPMI-7951 (line)]] | alt | 210 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -28.0) |
| [[SW 1271 (line)]] | alt | 228 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -15.1) |
| [[SW 900 (line)]] | alt | 265 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -25.4) |
| [[SW48 (line)]] | wt | 238 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -18.6) |
| [[H4 (line)]] | wt | 143 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -17.7) |
| [[CFPAC-1 (line)]] | alt | 206 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -16.3) |
| [[CHP-212 (line)]] | wt | 93.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -13.4) |
| [[HCT15 (line)]] | alt | 213 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -22.3) |
| [[hTERT-HPNE (line)]] | wt | 30.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 29.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 297 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 133 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1154), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDON]] | +0.76 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[PDK1]] | +0.75 | +0.83 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[HK2]] | +0.75 | +0.77 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[INSIG2]] | +0.74 | +0.80 / +0.59 | both halves | 7e-06 |  |
| [[PDK3]] | +0.74 | +0.77 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[GPR160]] | +0.73 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[ERO1A]] | +0.71 | +0.80 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[PLEKHA8]] | +0.71 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[UBE2Q2P2]] | +0.71 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[WASF3]] | +0.70 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[FAM234B]] | +0.70 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[ARL6]] | +0.69 | +0.72 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPRY3]] | -0.66 | -0.66 / -0.45 | both halves | 3e-05 |  |
| [[FIZ1]] | -0.65 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[ERCC6L2]] | -0.64 | -0.68 / -0.40 | both halves | 4e-05 |  |
| [[ITPA]] | -0.63 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[ZFY]] | -0.63 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[ZNF629]] | -0.63 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[MEPCE]] | -0.62 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[ITPRIPL2]] | -0.62 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[ZNF689]] | -0.62 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ZNF764]] | -0.62 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[EFCAB2]] | -0.61 | -0.65 / -0.34 | both halves | 1e-04 |  |
| [[HELQ]] | -0.61 | -0.61 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises TPD52's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.789). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.7, -16.2); signed map (-36.3, 24.0). **Vector** length 136, 48.1% of its response variance represented; |z| ≥ 3 in 1,309 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (control, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +10.0 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.8 | +5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +8.3 | +4.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.4 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +7.3 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.8 | +2.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.2 | +3.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.5 | -21.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.2 | -37.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.9 | -24.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.6 | -14.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.0 | -5.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.2 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.2 | -4.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.1 | -3.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | tumor protein D52 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:80,034,745-80,231,232 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D52, hD52, N8L |
| Hallmark sets | PROTEIN_SECRETION, ANDROGEN_RESPONSE, ALLOGRAFT_REJECTION, HYPOXIA |
| Reactome | 4 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

UniProt [P55327](https://www.uniprot.org/uniprotkb/P55327) carries no function annotation.

**Summary**, from NCBI Gene [7163](https://www.ncbi.nlm.nih.gov/gene/7163):

> Enables calcium ion binding activity and protein homodimerization activity. Involved in B cell differentiation. Located in endoplasmic reticulum and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:12005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12005) · Entrez [7163](https://www.ncbi.nlm.nih.gov/gene/7163) · UniProt [P55327](https://www.uniprot.org/uniprotkb/P55327) · Ensembl [ENSG00000076554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076554)

## Data

Gene col 1154: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1154); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1154, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1154]; `tensor/DDL_lfc|DDL_z.npy` [1154]; `embed/gene_vectors.npy` [1154]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1154 or target_col == 1154). Every well: [[TPD52 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPD52.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
