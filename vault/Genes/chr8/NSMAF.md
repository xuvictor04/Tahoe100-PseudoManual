---
symbol: "NSMAF"
type: "gene"
col: 431
ensembl_id: "ENSG00000035681"
name: "neutral sphingomyelinase activation associated factor"
location: "8q12.1"
module: 18
arm: "+"
pooled_cpm: 56.14
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# NSMAF

*neutral sphingomyelinase activation associated factor* — 8q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.07× (z +16.9, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.255× (z -35.8, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP46]] (+0.68, fdr 7e-06), [[RCC1L]] (+0.68, fdr 1e-05), [[KCTD15]] (+0.67, fdr 1e-05); moves opposite to [[RRAS]] (-0.62, fdr 3e-05), [[GNAI2]] (-0.59, fdr 1e-04), [[CDKN2D]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 431.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.07×** | +16.9 | 0e+00 | 44/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.79×** | +15.2 | 0e+00 | 44/48 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +14.0 | 1e-42 | 41/48 (HOP62, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +9.6 | 9e-20 | 42/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.97×** | +8.5 | 3e-15 | 31/43 (A498, RKO, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +6.7 | 1e-09 | 22/48 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.47×** | +5.9 | 3e-07 | 28/48 (HOP62, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +5.5 | 2e-06 | 24/48 (HOP62, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **1.42×** | +4.4 | 6e-04 | 16/48 (J82, COLO 205, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.3 | 0.001 | 18/48 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.2 | 0.002 | 16/48 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.003 | 16/48 (C32, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.11× | +4.0 | 0.003 | 11/48 (A498, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.0 | 0.003 | 13/47 (COLO 205, hTERT-HPNE, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +3.9 | 0.003 | 14/48 (NCI-H1792, C32, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.020 | 14/48 (C32, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.020 | 10/48 (MIA PaCa-2, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.043 | 6/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.13× | +3.2 | 0.043 | 9/47 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.13× | +3.1 | 0.045 | 14/48 (LOX-IMVI, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 431.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.255×** | -35.8 | 0e+00 | 46/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.258×** | -35.5 | 0e+00 | 47/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.332×** | -28.9 | 0e+00 | 45/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.542×** | -16.1 | 0e+00 | 40/48 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.767×** | -9.9 | 7e-21 | 36/48 (LS 180, C-33 A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.726×** | -8.4 | 4e-15 | 30/48 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 0.839× | -6.5 | 6e-09 | 24/48 (NCI-H1792, PANC-1, …) | top dose only | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.945× | -5.0 | 4e-05 | 1/49 (MIA PaCa-2) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.701×** | -4.5 | 5e-04 | 21/48 (C-33 A, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 0.841× | -4.4 | 7e-04 | 18/49 (RKO, SW48, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.843× | -4.3 | 8e-04 | 17/47 (RKO, SW48, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -4.0 | 0.003 | 17/48 (LS 180, C-33 A, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.761×** | -3.4 | 0.028 | 12/48 (C32, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | 0.884× | -3.2 | 0.047 | 18/46 (C32, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.885× | -3.2 | 0.052 | 10/49 (MIA PaCa-2, RKO, …) | two highest doses |  |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | 0.919× | -3.2 | 0.056 | 5/49 (HT-29, NCI-H661, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.822×** | -3.0 | 0.086 | 12/48 (Panc 03.27, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.892× | -3.0 | 0.087 | 12/48 (SNU-423, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 431. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 64.2 | 4 (1 ⚠) | 7 (3 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.28× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.191× (z -23.3) |
| [[MIA PaCa-2 (line)]] | alt | 77.6 | 3 (1 ⚠) | 6 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.38× (z +10.4) ⚠ unreliable plate only · without an alert: [[Bortezomib (drug)]] 0.05 µM 2.43× (z +9.4) | [[Panobinostat (drug)]] 5 µM 0.142× (z -23.4) |
| [[RKO (line)]] | wt | 189 | 0 | 9 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.190× (z -21.9) |
| [[A498 (line)]] | wt | 60.3 | 4 (1 ⚠) | 4 | [[Ixazomib citrate (drug)]] 5 µM 2.38× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.172× (z -22.8) |
| [[A-172 (line)]] | wt | 53.9 | 3 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +16.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.22× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.233× (z -15.5) |
| [[A-427 (line)]] | wt | 51.2 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.51× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.242× (z -15.5) |
| [[HOP62 (line)]] | alt | 47.5 | 4 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.314× (z -12.4) |
| [[PANC-1 (line)]] | alt | 43.7 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -18.5) |
| [[SW480 (line)]] | alt | 69.1 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -27.8) |
| [[C-33 A (line)]] | alt | 85.8 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.140× (z -20.2) |
| [[HEC-1-A (line)]] | alt | 58.1 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -19.2) |
| [[LoVo (line)]] | wt | 52.5 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.250× (z -16.1) |
| [[LS 180 (line)]] | wt | 77.4 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -25.0) |
| [[NCI-H2030 (line)]] | alt | 106 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -20.5) |
| [[SW48 (line)]] | wt | 131 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -21.2) |
| [[C32 (line)]] | wt | 101 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.243× (z -17.1) |
| [[HS-578T (line)]] | alt | 60.4 | 1 | 3 | [[Ixazomib citrate (drug)]] 5 µM 2.35× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.215× (z -16.0) |
| [[J82 (line)]] | alt | 63.5 | 1 (1 ⚠) | 3 | [[Niclosamide (olamine) (drug)]] 5 µM 2.46× (z +9.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.205× (z -17.3) |
| [[SNU-1 (line)]] | wt | 112 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.173× (z -17.0) |
| [[A549 (line)]] | wt | 56.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -16.5) |
| [[AN3 CA (line)]] | alt | 73.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.231× (z -8.5) |
| [[COLO 205 (line)]] | alt | 31.0 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 5.80× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.213× (z -9.2) |
| [[H4 (line)]] | wt | 47.0 | 1 | 2 | [[Ixazomib citrate (drug)]] 5 µM 3.59× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.222× (z -10.4) |
| [[HT-29 (line)]] | alt | 27.5 | 1 | 2 | [[Bortezomib (drug)]] 0.05 µM 3.59× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.275× (z -10.5) |
| [[KATO III (line)]] | alt | 43.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -19.2) |
| [[LOX-IMVI (line)]] | wt | 49.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 50.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -16.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.281× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 32.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 45.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -12.3) |
| [[SHP-77 (line)]] | alt | 72.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.255× (z -14.9) |
| [[SNU-423 (line)]] | alt | 49.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -14.0) |
| [[SW 900 (line)]] | alt | 64.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -12.9) |
| [[SW1417 (line)]] | alt | 38.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -13.8) |
| [[Hs 766T (line)]] | wt | 37.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 25.1 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.07× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -9.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H2347 (line)]] | alt | 26.6 | 1 | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.39× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.420× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 45.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -9.9) |
| [[BT-474 (line)]] | alt | 59.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -13.4) |
| [[CHP-212 (line)]] | wt | 68.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -10.1) |
| [[SW 1271 (line)]] | alt | 52.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0794× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 431), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP46]] | +0.68 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[RCC1L]] | +0.68 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[KCTD15]] | +0.67 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[QRSL1]] | +0.66 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[RHBDD3]] | +0.66 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[IDE]] | +0.66 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[PRMT3]] | +0.64 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SLC9B2]] | +0.63 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[HDDC2]] | +0.63 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[ZFYVE9]] | +0.63 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[ZNF346]] | +0.63 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[MVB12B]] | +0.62 | +0.61 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAS]] | -0.62 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[GNAI2]] | -0.59 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[CDKN2D]] | -0.58 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[SPAG9]] | -0.58 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[PJA2]] | -0.57 | -0.37 / -0.49 | both halves | 9e-05 |  |
| [[NBEAL1]] | -0.56 | -0.48 / -0.35 | both halves | 1e-04 | same gene group |
| [[LGALS1]] | -0.56 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[FAM89B]] | -0.55 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[RING1]] | -0.55 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[ILK]] | -0.55 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[PLAG1]] | -0.55 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[DDAH2]] | -0.54 | -0.51 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises NSMAF's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises NSMAF's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PC]] | C | PC activity lowers NSMAF's level | lines that do not express PC (4) vs lines expressing it (46) | 2.48× higher at baseline in the lines without PC | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: DUSP1, ANKEF1, ZFAND4; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-10.1, 14.7); signed map (12.2, -44.3). **Vector** length 121, 34.7% of its response variance represented; |z| ≥ 3 in 1,163 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +11.3 | +15.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +11.3 | +16.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.4 | +14.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.3 | +9.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.9 | -0.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.8 | +5.9 |
|  | [[EX229 (drug)]] 5 µM |  | +4.3 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.1 | +3.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.6 | -35.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.2 | -28.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -35.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -9.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.9 | -16.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -2.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.0 | -3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | neutral sphingomyelinase activation associated factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q12.1 — chr8:58,583,508-58,659,853 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FAN, GRAMD5 |
| Gene groups (HGNC) | WD repeat domain containing; GRAM domain containing; BEACH domain containing |
| Reactome | 3 pathways, smallest: TNFR1-mediated ceramide production; TNF signaling; Death Receptor Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92636](https://www.uniprot.org/uniprotkb/Q92636) (Protein FAN):

> Couples the p55 TNF-receptor (TNF-R55 / TNFR1) to neutral sphingomyelinase (N-SMASE). Specifically binds to the N-smase activation domain of TNF-R55. May regulate ceramide production by N-SMASE.

**Summary**, from NCBI Gene [8439](https://www.ncbi.nlm.nih.gov/gene/8439):

> This gene encodes a WD-repeat protein that binds the cytoplasmic sphingomyelinase activation domain of the 55kD tumor necrosis factor receptor. This protein is required for TNF-mediated activation of neutral sphingomyelinase and may play a role in regulating TNF-induced cellular responses such as inflammation. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:8017](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8017) · Entrez [8439](https://www.ncbi.nlm.nih.gov/gene/8439) · UniProt [Q92636](https://www.uniprot.org/uniprotkb/Q92636) · Ensembl [ENSG00000035681](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000035681)

## Data

Gene col 431: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 431); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 431, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 431]; `tensor/DDL_lfc|DDL_z.npy` [431]; `embed/gene_vectors.npy` [431]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 431 or target_col == 431). Every well: [[NSMAF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSMAF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
