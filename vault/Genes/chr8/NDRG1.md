---
symbol: "NDRG1"
type: "gene"
col: 2459
ensembl_id: "ENSG00000104419"
name: "N-myc downstream regulated 1"
location: "8q24.22"
module: 180
arm: "+"
pooled_cpm: 1001.67
n_lines_expressing: 44
n_dd_up: 7
n_dd_down: 29
n_dd_up_clean: 7
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 21
direction_downstream: 44
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# NDRG1

*N-myc downstream regulated 1* — 8q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.54× (z +7.1, q 6e-10, up in 39 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.171× (z -29.2, q 0e+00, down in 40 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD37]] (+0.80, fdr 7e-06), [[INSIG2]] (+0.75, fdr 7e-06), [[ENO2]] (+0.73, fdr 7e-06); moves opposite to [[UTP20]] (-0.69, fdr 7e-06), [[MCCC2]] (-0.68, fdr 7e-06), [[ZMYND11]] (-0.68, fdr 1e-05).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 44 go from it, the strongest it → [[CARD19]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2459.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.54×** | +7.1 | 6e-10 | 39/42 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.55×** | +5.0 | 2e-04 | 41/42 (AsPC-1, LS 180, …) | rises with dose | plate-row cell shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +4.8 | 3e-04 | 37/43 (LS 180, RKO, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.47×** | +4.3 | 0.002 | 39/43 (AsPC-1, HT-29, …) | top dose only | plate-row cell shift |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.011 | 33/41 (RKO, LOX-IMVI, …) | two highest doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.79×** | +3.6 | 0.035 | 31/42 (CHP-212, HT-29, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Fumaric acid (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.054 | 36/43 (AsPC-1, NCI-H2122, …) | top dose only | plate-row cell shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.31× | +3.0 | 0.17 | 24/41 (RKO, LOX-IMVI, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2459.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.171×** | -29.2 | 0e+00 | 40/42 (HT-29, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.205×** | -17.8 | 0e+00 | 42/42 (NCI-H1573, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.227×** | -16.7 | 0e+00 | 41/41 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.253×** | -16.1 | 0e+00 | 42/42 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.252×** | -15.5 | 0e+00 | 36/38 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.305×** | -13.9 | 8e-42 | 39/43 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.314×** | -12.5 | 5e-34 | 36/39 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.387×** | -11.1 | 8e-27 | 42/42 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.373×** | -11.1 | 8e-27 | 39/41 (HT-29, H4, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.592×** | -8.7 | 3e-16 | 36/43 (SNU-423, HS-578T, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.641×** | -7.4 | 9e-12 | 35/42 (NCI-H1573, SW48, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.554×** | -6.9 | 2e-10 | 33/42 (HEC-1-A, C32, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.679×** | -6.4 | 7e-09 | 36/42 (A-172, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.670×** | -4.7 | 1e-04 | 30/42 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.675×** | -4.6 | 2e-04 | 34/42 (LOX-IMVI, SK-MEL-2, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.677×** | -4.6 | 2e-04 | 35/42 (A-172, KATO III, …) | inconsistent across doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.773×** | -4.3 | 7e-04 | 29/42 (A549, HOP62, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.520×** | -4.0 | 0.002 | 30/42 (MIA PaCa-2, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.715×** | -3.9 | 0.003 | 30/42 (H4, NCI-H1573, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.726×** | -3.8 | 0.005 | 24/42 (A-172, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.596×** | -3.2 | 0.038 | 23/42 (AsPC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.765×** | -3.1 | 0.038 | 24/42 (HCT15, SW48, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.766×** | -2.9 | 0.075 | 25/41 (CFPAC-1, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.784×** | -2.8 | 0.084 | 25/42 (HepG2/C3A, BT-474, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.65 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2459. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 3,205 | 1 | 13 (8 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.94× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -25.5) |
| [[HT-29 (line)]] | alt | 2,053 | 1 (1 ⚠) | 13 (9 ⚠) | [[Daptomycin (drug)]] 5 µM 2.43× (z +8.6) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.0748× (z -35.7) |
| [[SNU-423 (line)]] | alt | 1,170 | 0 | 14 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0913× (z -34.8) |
| [[A-172 (line)]] | wt | 1,352 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0800× (z -30.6) |
| [[A549 (line)]] | wt | 1,236 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -31.8) |
| [[hTERT-HPNE (line)]] | wt | 1,606 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -22.5) |
| [[RPMI-7951 (line)]] | alt | 1,978 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -26.2) |
| [[HOP62 (line)]] | alt | 2,022 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -24.6) |
| [[C32 (line)]] | wt | 1,586 | 0 | 10 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.143× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 1,583 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -30.1) |
| [[H4 (line)]] | wt | 1,705 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -24.3) |
| [[HCT15 (line)]] | alt | 1,512 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0443× (z -34.6) |
| [[Hs 766T (line)]] | wt | 2,011 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0996× (z -35.5) |
| [[LOX-IMVI (line)]] | wt | 818 | 1 | 9 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.13× (z +11.3) | [[Harringtonine (drug)]] 5 µM 0.199× (z -16.4) |
| [[NCI-H2347 (line)]] | alt | 2,297 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -29.5) |
| [[SW 900 (line)]] | alt | 1,257 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -24.4) |
| [[LS 180 (line)]] | wt | 1,010 | 2 | 7 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.25× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -27.5) |
| [[NCI-H1573 (line)]] | alt | 1,645 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -28.8) |
| [[NCI-H1792 (line)]] | alt | 890 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -15.5) |
| [[Panc 03.27 (line)]] | alt | 845 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -17.8) |
| [[COLO 205 (line)]] | alt | 859 | 2 (1 ⚠) | 6 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.13× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -20.5) |
| [[HEC-1-A (line)]] | alt | 756 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -25.3) |
| [[HepG2_C3A (line)]] | wt | 676 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -25.7) |
| [[J82 (line)]] | alt | 1,245 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -17.5) |
| [[CHP-212 (line)]] | wt | 661 | 1 | 6 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.21× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.0796× (z -27.5) |
| [[RKO (line)]] | wt | 411 | 4 (1 ⚠) | 3 | [[Tucidinostat (drug)]] 5 µM 2.68× (z +11.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.346× (z -9.0) |
| [[SW48 (line)]] | wt | 762 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -20.8) |
| [[BT-474 (line)]] | alt | 745 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -24.0) |
| [[SK-MEL-2 (line)]] | alt | 591 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -21.1) |
| [[AsPC-1 (line)]] | alt | 1,642 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -30.1) |
| [[KATO III (line)]] | alt | 743 | 1 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.97× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -19.0) |
| [[LoVo (line)]] | wt | 439 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -23.8) |
| [[MIA PaCa-2 (line)]] | alt | 327 | 1 | 4 | [[Tucidinostat (drug)]] 5 µM 2.07× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -16.8) |
| [[NCI-H460 (line)]] | wt | 519 | 1 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.21× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -17.7) |
| [[SW 1088 (line)]] | alt | 1,482 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -12.5) |
| [[SW480 (line)]] | alt | 388 | 1 | 4 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.20× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -15.8) |
| [[NCI-H2030 (line)]] | alt | 342 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -15.0) |
| [[SHP-77 (line)]] | alt | 847 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -19.0) |
| [[SW 1271 (line)]] | alt | 486 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -12.8) |
| [[A498 (line)]] | wt | 871 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.346× (z -9.7) ⚠ toxic |
| [[SW1417 (line)]] | alt | 513 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.402× (z -9.5) |
| [[A-427 (line)]] | wt | 80.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 285 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 99.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1,540 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 217 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1,108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 130 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 188 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 122 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2459), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD37]] | +0.80 | +0.82 / +0.74 | both halves | 7e-06 | STRING 425 |
| [[INSIG2]] | +0.75 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[ENO2]] | +0.73 | +0.79 / +0.58 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[UBE2O]] | +0.72 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[SLC17A7]] | +0.72 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[NGLY1]] | +0.71 | +0.76 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[P4HA1]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 495 |
| [[CIB1]] | +0.70 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[HILPDA]] | +0.70 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[PFKFB3]] | +0.69 | +0.66 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[KDM4B]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[BNIP3L]] | +0.68 | +0.80 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP20]] | -0.69 | -0.65 / -0.62 | both halves | 7e-06 |  |
| [[MCCC2]] | -0.68 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[ZMYND11]] | -0.68 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[GTF3C6]] | -0.67 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[ZNF507]] | -0.66 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[POGLUT1]] | -0.66 | -0.71 / -0.54 | both halves | 1e-05 |  |
| [[MAPKAPK5]] | -0.63 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[UTP15]] | -0.63 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[ABCE1]] | -0.63 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[DIS3L]] | -0.62 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[ZNF644]] | -0.62 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[QTRT1]] | -0.61 | -0.55 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 18, C 3. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NDRG1's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.9% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[CFAP45]] | B | CFAP45 activity raises NDRG1's level | lines that do not express CFAP45 (6) vs lines expressing it (44) | 4.16× lower at baseline in the lines without CFAP45 | 0.007 | ⚠ within organs, on part of the lines; also absent: STAMBPL1, RNASEL, RUNX1; maybe low, not absent |
| [[EHD2]] | B | EHD2 activity raises NDRG1's level | lines that do not express EHD2 (14) vs lines expressing it (36) | 2.86× lower at baseline in the lines without EHD2 | 0.008 | ⚠ within organs, on part of the lines; also absent: ITGA3, ENSG00000289526, ENSG00000230479 |
| [[PLOD2]] | B | PLOD2 activity raises NDRG1's level | lines that do not express PLOD2 (15) vs lines expressing it (35) | 2.58× lower at baseline in the lines without PLOD2 | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGA1, TMEM92-AS1, RGS17 |
| [[GRB10]] | B | GRB10 activity raises NDRG1's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 3.02× lower at baseline in the lines without GRB10 | 0.013 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[FAM13A]] | B | FAM13A activity raises NDRG1's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 2.58× lower at baseline in the lines without FAM13A | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[CDK18]] | B | CDK18 activity raises NDRG1's level | lines that do not express CDK18 (9) vs lines expressing it (41) | 2.98× lower at baseline in the lines without CDK18 | 0.040 | ⚠ within organs, on part of the lines; also absent: LINC00511, ABCG2, CYP2J2; maybe low, not absent |
| [[DEPP1]] | B | DEPP1 activity raises NDRG1's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 2.10× lower at baseline in the lines without DEPP1 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[BACE2]] | B | BACE2 activity raises NDRG1's level | lines that do not express BACE2 (10) vs lines expressing it (40) | 3.04× lower at baseline in the lines without BACE2 | 0.043 | ⚠ within organs, on part of the lines; also absent: FBXO32, STAT5A, ETS2 |
| [[TNFRSF11A]] | B | TNFRSF11A activity raises NDRG1's level | lines that do not express TNFRSF11A (9) vs lines expressing it (41) | 2.09× lower at baseline in the lines without TNFRSF11A | 0.045 | ⚠ within organs, on part of the lines; also absent: PTGER4; maybe low, not absent |
| [[PAG1]] | B | PAG1 activity raises NDRG1's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 2.47× lower at baseline in the lines without PAG1 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| [[TTYH2]] | B | TTYH2 activity lowers NDRG1's level | lines that do not express TTYH2 (9) vs lines expressing it (41) | 2.09× higher at baseline in the lines without TTYH2 | 0.058 | ⚠ within organs, on part of the lines; also absent: DUXAP8, DUXAP10, DUXAP9; maybe low, not absent |

### Downstream of this gene

*44 arrows, 44 of them with an alert ⚠; grade A 0, B 42, C 2. Shown: the 12 strongest; 32 more arrows (32 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CARD19]] | B | NDRG1 activity raises CARD19's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 2.27× lower at baseline in the lines without NDRG1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[SENP1]] | B | NDRG1 activity lowers SENP1's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.77× higher at baseline in the lines without NDRG1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[PDXK]] | B | NDRG1 activity raises PDXK's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.91× lower at baseline in the lines without NDRG1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[DEDD2]] | B | NDRG1 activity raises DEDD2's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without NDRG1 | 0.013 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[ABCE1]] | B | NDRG1 activity lowers ABCE1's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.64× higher at baseline in the lines without NDRG1 | 0.016 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[UTP20]] | B | NDRG1 activity lowers UTP20's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.86× higher at baseline in the lines without NDRG1 | 0.017 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[GTF3C6]] | B | NDRG1 activity lowers GTF3C6's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.73× higher at baseline in the lines without NDRG1 | 0.017 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[ZNF236]] | B | NDRG1 activity lowers ZNF236's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.96× higher at baseline in the lines without NDRG1 | 0.017 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[METAP1D]] | B | NDRG1 activity lowers METAP1D's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 2.06× higher at baseline in the lines without NDRG1 | 0.017 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[SERPINB1]] | B | NDRG1 activity raises SERPINB1's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 3.42× lower at baseline in the lines without NDRG1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[XPNPEP1]] | B | NDRG1 activity raises XPNPEP1's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 1.38× lower at baseline in the lines without NDRG1 | 0.021 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[RNF24]] | B | NDRG1 activity raises RNF24's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 2.26× lower at baseline in the lines without NDRG1 | 0.025 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.814). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.2, -15.1); signed map (-35.4, 25.5). **Vector** length 148, 60.5% of its response variance represented; |z| ≥ 3 in 1,737 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +12.1 | +7.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +9.5 | -2.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +9.2 | -0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +9.2 | -6.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +9.0 | +4.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +5.6 | +3.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.6 | +1.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.2 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.0 | +3.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.6 | -17.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -7.3 | -11.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.0 | -16.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.9 | -11.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -5.1 | -3.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.3 | -2.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -4.2 | -2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -4.0 | -4.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | N-myc downstream regulated 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.22 — chr8:133,237,175-133,302,022 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DRG1, RTP, TDD5, NDR1; previously CAP43 |
| Gene groups (HGNC) | NDRG family |
| Hallmark sets | ANDROGEN_RESPONSE, IL2_STAT5_SIGNALING, HYPOXIA, P53_PATHWAY |
| Reactome | 3 pathways, smallest: TP53 regulates transcription of several additional cell death genes whose specific roles in p53-dependent apoptosis remain uncertain; TP53 Regulates Transcription of Cell Death Genes; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92597](https://www.uniprot.org/uniprotkb/Q92597) (Protein NDRG1):

> Stress-responsive protein involved in hormone responses, cell growth, and differentiation. Acts as a tumor suppressor in many cell types. Necessary but not sufficient for p53/TP53-mediated caspase activation and apoptosis. Has a role in cell trafficking, notably of the Schwann cell, and is necessary for the maintenance and development of the peripheral nerve myelin sheath. Required for vesicular recycling of CDH1 and TF. May also function in lipid trafficking. Protects cells from spindle …

**Summary**, from NCBI Gene [10397](https://www.ncbi.nlm.nih.gov/gene/10397):

> This gene is a member of the N-myc downregulated gene family which belongs to the alpha/beta hydrolase superfamily. The protein encoded by this gene is a cytoplasmic protein involved in stress responses, hormone responses, cell growth, and differentiation. The encoded protein is necessary for p53-mediated caspase activation and apoptosis. Mutations in this gene are a cause of Charcot-Marie-Tooth disease type 4D, and expression of this gene may be a prognostic indicator for several types of …

**Accessions** — [HGNC:7679](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7679) · Entrez [10397](https://www.ncbi.nlm.nih.gov/gene/10397) · UniProt [Q92597](https://www.uniprot.org/uniprotkb/Q92597) · Ensembl [ENSG00000104419](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104419)

## Data

Gene col 2459: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2459); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2459, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2459]; `tensor/DDL_lfc|DDL_z.npy` [2459]; `embed/gene_vectors.npy` [2459]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2459 or target_col == 2459). Every well: [[NDRG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDRG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
