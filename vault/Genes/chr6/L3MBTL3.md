---
symbol: "L3MBTL3"
type: "gene"
col: 12750
ensembl_id: "ENSG00000198945"
name: "L3MBTL histone methyl-lysine binding protein 3"
location: "6q23.1"
module: 18
arm: "+"
pooled_cpm: 11.52
n_lines_expressing: 48
n_dd_up: 27
n_dd_down: 12
n_dd_up_clean: 21
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# L3MBTL3

*L3MBTL histone methyl-lysine binding protein 3* — 6q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.31× (z +31.6, q 0e+00, up in 43 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.342× (z -23.2, q 0e+00, down in 39 of 43 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.309× (z -17.9, q 0e+00, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP3R1]] (+0.58, fdr 1e-05), [[CSNK1G3]] (+0.57, fdr 1e-05), [[MFAP3L]] (+0.55, fdr 5e-05); moves opposite to [[CHMP4A]] (-0.57, fdr 2e-05), [[RELB]] (-0.54, fdr 1e-05), [[ZNF136]] (-0.52, fdr 6e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12750.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.31×** | +31.6 | 0e+00 | 43/43 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.67×** | +21.3 | 0e+00 | 42/45 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.86×** | +16.0 | 0e+00 | 40/45 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.28×** | +15.6 | 0e+00 | 41/43 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +10.4 | 4e-23 | 33/42 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +8.6 | 6e-16 | 27/41 (SW480, C32, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.76×** | +8.6 | 6e-16 | 33/42 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.75×** | +8.5 | 1e-15 | 26/44 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.68×** | +7.9 | 1e-13 | 29/45 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +7.6 | 2e-12 | 24/45 (HOP62, A498, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.23×** | +6.4 | 7e-09 | 24/44 (PANC-1, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +5.7 | 5e-07 | 17/43 (A498, HEC-1-A, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.42×** | +5.4 | 3e-06 | 15/45 (A498, SW480, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.28×** | +5.4 | 3e-06 | 18/45 (A-427, NCI-H1792, …) | top dose only | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.39×** | +5.0 | 2e-05 | 13/43 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +3.8 | 0.005 | 12/44 (LOX-IMVI, A-172, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.59×** | +3.7 | 0.006 | 6/42 (J82, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12750.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.342×** | -23.2 | 0e+00 | 39/43 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.309×** | -17.9 | 0e+00 | 39/45 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.373×** | -15.1 | 0e+00 | 37/43 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.396×** | -13.6 | 4e-40 | 35/44 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.357×** | -13.6 | 5e-40 | 35/42 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.504×** | -10.5 | 8e-24 | 30/43 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.507×** | -10.4 | 2e-23 | 31/43 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.539×** | -9.5 | 2e-19 | 29/43 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.655×** | -6.5 | 6e-09 | 23/44 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.542×** | -4.9 | 6e-05 | 15/43 (C-33 A, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.617×** | -3.9 | 0.006 | 16/43 (NCI-H2030, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.789×** | -3.6 | 0.014 | 13/45 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12750. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 14.9 | 4 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.15× (z +19.7) | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -16.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -10.0) |
| [[LoVo (line)]] | wt | 23.9 | 2 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +18.5) | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -17.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -16.4) |
| [[NCI-H2030 (line)]] | alt | 23.3 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -21.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0964× (z -17.0) |
| [[LOX-IMVI (line)]] | wt | 39.1 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -19.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -15.0) |
| [[MIA PaCa-2 (line)]] | alt | 11.8 | 1 | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.98× (z +13.5) | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -11.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.160× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 9.26 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.35× (z +15.3) | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -11.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.214× (z -9.0) |
| [[SW1417 (line)]] | alt | 18.5 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.43× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -14.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0894× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 16.1 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +15.9) | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 9.39 | 2 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.29× (z +14.1) | [[Docetaxel (drug)]] 0.05 µM 0.0849× (z -13.4) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 21.8 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -15.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[PANC-1 (line)]] | alt | 4.28 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 5.96× (z +12.4) | — |
| [[RKO (line)]] | wt | 13.5 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.0671× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0794× (z -10.1) |
| [[J82 (line)]] | alt | 10.1 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 7.42 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.68× (z +10.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.0982× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -12.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0797× (z -12.4) |
| [[Hs 766T (line)]] | wt | 7.21 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.0600× (z -10.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 9.88 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.87× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -10.1) ⚠ cell-cycle shift, explains ~28% of this change |
| [[NCI-H1792 (line)]] | alt | 14.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -10.2) |
| [[SW48 (line)]] | wt | 30.8 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0739× (z -13.7) |
| [[A-172 (line)]] | wt | 10.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.81× (z +10.0) | — |
| [[A498 (line)]] | wt | 8.70 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -10.5) ⚠ cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 6.58 | 0 | 1 (1 ⚠) | — | [[Pentoxifylline (drug)]] 0.05 µM 0.0739× (z -9.4) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 7.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.92× (z +9.4) | — |
| [[C32 (line)]] | wt | 6.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.16× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 6.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +10.1) | — |
| [[COLO 205 (line)]] | alt | 8.73 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +8.8) | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -8.5) |
| [[HCT15 (line)]] | alt | 7.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.84× (z +9.5) | — |
| [[HS-578T (line)]] | alt | 5.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.43× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 9.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 16.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0922× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -13.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[RPMI-7951 (line)]] | alt | 4.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +10.4) | — |
| [[SK-MEL-2 (line)]] | alt | 7.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +10.3) | — |
| [[SNU-423 (line)]] | alt | 8.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.11× (z +11.2) | — |
| [[A-427 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12750), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP3R1]] | +0.58 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[CSNK1G3]] | +0.57 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[MFAP3L]] | +0.55 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[SCD5]] | +0.54 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[TBC1D4]] | +0.54 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[PALS2]] | +0.54 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[GRB2]] | +0.53 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[RREB1]] | +0.52 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[DOCK9]] | +0.52 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[CDYL]] | +0.52 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[ANKRD13B]] | +0.52 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[SLC39A6]] | +0.51 | +0.40 / +0.51 | both halves | 5e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP4A]] | -0.57 | -0.46 / -0.63 | both halves | 2e-05 |  |
| [[RELB]] | -0.54 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[ZNF136]] | -0.52 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[SPG11]] | -0.52 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[SPEF2]] | -0.51 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[MAPK1IP1L]] | -0.51 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[DHRSX]] | -0.50 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[MKS1]] | -0.50 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[DNAL4]] | -0.50 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[BBS1]] | -0.50 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[ZNF776]] | -0.49 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[ZNF140]] | -0.49 | -0.43 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers L3MBTL3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.336). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-7.2, -4.2); signed map (-36.1, -18.6). **Vector** length 94.9, 22.1% of its response variance represented; |z| ≥ 3 in 1,171 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +31.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +9.2 | +21.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.7 | +15.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.3 | +16.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.0 | +8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +5.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.5 | +7.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.4 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +7.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -7.1 | -23.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.1 | -13.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -13.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.9 | -9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -6.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | L3MBTL histone methyl-lysine binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.1 — chr6:130,013,699-130,141,449 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1798 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; Zinc fingers C2H2C-type; MBT domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JM7](https://www.uniprot.org/uniprotkb/Q96JM7) (Lethal(3)malignant brain tumor-like protein 3):

> Is a negative regulator of Notch target genes expression, required for RBPJ-mediated transcriptional repression. It recruits KDM1A to Notch-responsive elements and promotes KDM1A-mediated H3K4me demethylation. Involved in the regulation of ubiquitin-dependent degradation of a set of methylated non-histone proteins, including SOX2, DNMT1 and E2F1. It acts as an adapter recruiting the CRL4-DCAF5 E3 ubiquitin ligase complex to methylated target proteins. Required for normal maturation of myeloid …

**Summary**, from NCBI Gene [84456](https://www.ncbi.nlm.nih.gov/gene/84456):

> This gene encodes a member of the malignant brain tumor (MBT) family of chromatin interacting transcriptional repressors. Members of this family function as methyl-lysine readers, which recognize methylated lysine residues on histone protein tails, and are associated with the repression of gene expression. The encoded protein may regulate hematopoiesis. Homozygous deletion of this gene has been observed in human patients with medulloblastoma. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:23035](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23035) · Entrez [84456](https://www.ncbi.nlm.nih.gov/gene/84456) · UniProt [Q96JM7](https://www.uniprot.org/uniprotkb/Q96JM7) · Ensembl [ENSG00000198945](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198945)

## Data

Gene col 12750: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12750); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12750, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12750]; `tensor/DDL_lfc|DDL_z.npy` [12750]; `embed/gene_vectors.npy` [12750]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12750 or target_col == 12750). Every well: [[L3MBTL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/L3MBTL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
