---
symbol: "LITAF"
type: "gene"
col: 12086
ensembl_id: "ENSG00000189067"
name: "lipopolysaccharide induced TNF factor"
location: "16p13.13"
module: 14
arm: "+"
pooled_cpm: 103.63
n_lines_expressing: 47
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 16
direction_downstream: 5
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# LITAF

*lipopolysaccharide induced TNF factor* — 16p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.92× (z +15.8, q 0e+00, up in 32 of 45 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 2.09× (z +12.1, q 4e-31, up in 32 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.493× (z -12.1, q 4e-31, down in 39 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMO]] (+0.69, fdr 7e-06), [[LGALS3]] (+0.68, fdr 7e-06), [[TNFAIP2]] (+0.65, fdr 7e-06); moves opposite to [[FBXW2]] (-0.67, fdr 1e-05), [[ABHD17A]] (-0.63, fdr 3e-05), [[RNGTT]] (-0.63, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[RASEF]] → it (grade B ⚠); 5 go from it, the strongest it → cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12086.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.92×** | +15.8 | 0e+00 | 32/45 (HOP62, CFPAC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.09×** | +12.1 | 4e-31 | 32/45 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.84×** | +10.5 | 3e-23 | 30/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +8.0 | 2e-13 | 32/45 (C32, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.41×** | +5.8 | 6e-07 | 28/45 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +5.7 | 9e-07 | 24/39 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +5.0 | 4e-05 | 24/45 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +4.6 | 3e-04 | 26/45 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.31×** | +4.5 | 3e-04 | 25/44 (NCI-H1573, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.9 | 0.005 | 19/46 (NCI-H460, HepG2/C3A, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.014 | 16/45 (NCI-H1573, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.068 | 16/45 (NCI-H1573, BT-474, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12086.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.493×** | -12.1 | 4e-31 | 39/45 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.496×** | -12.0 | 6e-31 | 40/45 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.563×** | -9.9 | 1e-20 | 40/45 (A498, HT-29, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Folic acid (drug)]] 5 µM |  | 0.863× | -3.6 | 0.043 | 11/45 (Hs 766T, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.832× | -3.2 | 0.15 | 18/45 (HT-29, SNU-423, …) | all doses, stronger at high dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.833× | -3.2 | 0.15 | 15/44 (HT-29, A498, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12086. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 76.9 | 13 (7 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +25.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 8.45× (z +21.7) | [[Panobinostat (drug)]] 0.5 µM 0.306× (z -12.0) |
| [[BT-474 (line)]] | alt | 150 | 7 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +17.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.24× (z +11.9) | [[Panobinostat (drug)]] 0.5 µM 0.426× (z -9.0) |
| [[A498 (line)]] | wt | 451 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 0.5 µM 2.87× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.181× (z -24.4) |
| [[SNU-423 (line)]] | alt | 130 | 4 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +23.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.28× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.213× (z -14.8) |
| [[A-172 (line)]] | wt | 82.6 | 4 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 6.44× (z +18.2) | [[Panobinostat (drug)]] 5 µM 0.304× (z -11.6) |
| [[J82 (line)]] | alt | 103 | 4 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 7.08× (z +27.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.96× (z +17.3) | [[Panobinostat (drug)]] 0.5 µM 0.333× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 129 | 4 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 3.96× (z +18.3) | [[Panobinostat (drug)]] 0.5 µM 0.468× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 78.3 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +21.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.54× (z +15.9) | — |
| [[HEC-1-A (line)]] | alt | 180 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +12.7) | — |
| [[HepG2_C3A (line)]] | wt | 151 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +16.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.98× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 226 | 2 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +14.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.88× (z +13.5) | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -14.6) |
| [[PANC-1 (line)]] | alt | 64.5 | 4 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.92× (z +26.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 7.66× (z +23.5) | [[Panobinostat (drug)]] 5 µM 0.454× (z -9.2) |
| [[HOP62 (line)]] | alt | 69.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.51× (z +30.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.76× (z +15.8) | — |
| [[Hs 766T (line)]] | wt | 134 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +11.7) ⚠ cell-cycle shift, explains ~28% of this change | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -13.0) |
| [[HS-578T (line)]] | alt | 41.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +14.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.46× (z +13.2) | — |
| [[HT-29 (line)]] | alt | 183 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.157× (z -22.3) |
| [[NCI-H1573 (line)]] | alt | 116 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +12.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.73× (z +12.0) | — |
| [[A549 (line)]] | wt | 147 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.242× (z -14.4) |
| [[hTERT-HPNE (line)]] | wt | 33.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.26× (z +17.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 13.1× (z +14.7) | — |
| [[RKO (line)]] | wt | 62.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.357× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 71.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +15.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.43× (z +11.8) | — |
| [[A-427 (line)]] | wt | 58.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.402× (z -9.1) |
| [[C32 (line)]] | wt | 120 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.95× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 118 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.32× (z +29.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.08× (z +15.3) | — |
| [[NCI-H1792 (line)]] | alt | 67.8 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.14× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 74.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.65× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 27.4 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.262× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 237 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 2.73× (z +9.3) | [[Panobinostat (drug)]] 0.5 µM 0.401× (z -8.8) |
| [[SW 900 (line)]] | alt | 70.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.283× (z -9.5) |
| [[SW1417 (line)]] | alt | 99.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.484× (z -8.6) |
| [[H4 (line)]] | wt | 62.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[LoVo (line)]] | wt | 36.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.380× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 57.7 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +9.4) | — |
| [[NCI-H596 (line)]] | alt | 84.6 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.165× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 42.5 | 0 | 1 | — | [[Vismodegib (drug)]] 0.5 µM 0.0743× (z -9.0) |
| [[SW480 (line)]] | alt | 42.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.27× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 114 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.3 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 85.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.84 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 68.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.15 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12086), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMO]] | +0.69 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[LGALS3]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[TNFAIP2]] | +0.65 | +0.62 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SLC2A6]] | +0.62 | +0.69 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[STAT5A]] | +0.62 | +0.54 / +0.51 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[GATA6]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[MAP3K2-DT]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[STAP2]] | +0.61 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[RRAD]] | +0.60 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[FBXO32]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[DRAM1]] | +0.60 | +0.58 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SLCO2B1]] | +0.59 | +0.51 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW2]] | -0.67 | -0.64 / -0.55 | both halves | 1e-05 |  |
| [[ABHD17A]] | -0.63 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[RNGTT]] | -0.63 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[WDR5]] | -0.60 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[DROSHA]] | -0.60 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[ACTR5]] | -0.59 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[BLTP2]] | -0.57 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[INTS11]] | -0.57 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[NOC2L]] | -0.56 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[ATG16L1]] | -0.56 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[BCAP31]] | -0.56 | -0.58 / -0.43 | both halves | 4e-05 |  |
| [[TSFM]] | -0.55 | -0.50 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASEF]] | B | RASEF activity raises LITAF's level | lines that do not express RASEF (20) vs lines expressing it (30) | 2.09× lower at baseline in the lines without RASEF | 0.007 | ⚠ within organs, on part of the lines; also absent: LIPH, ENSG00000263325, DENND2D |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises LITAF's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.31× lower at baseline in the lines without ELF3-AS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[LGALS3]] | B | LGALS3 activity raises LITAF's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 2.43× lower at baseline in the lines without LGALS3 | 0.020 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[LINC02967]] | B | LINC02967 activity raises LITAF's level | lines that do not express LINC02967 (34) vs lines expressing it (16) | 1.59× lower at baseline in the lines without LINC02967 | 0.024 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4 |
| [[HDAC6]] | B | HDAC6 activity raises LITAF's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CX3CL1]] | B | CX3CL1 activity raises LITAF's level | lines that do not express CX3CL1 (28) vs lines expressing it (22) | 1.82× lower at baseline in the lines without CX3CL1 | 0.030 | ⚠ within organs, on part of the lines; also absent: SHROOM4, GRIN2A, GPNMB |
| [[CGNL1]] | B | CGNL1 activity raises LITAF's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.80× lower at baseline in the lines without CGNL1 | 0.039 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[PRRG4]] | B | PRRG4 activity raises LITAF's level | lines that do not express PRRG4 (16) vs lines expressing it (34) | 1.83× lower at baseline in the lines without PRRG4 | 0.042 | ⚠ within organs, on part of the lines; also absent: BIK, MYO5B, ERBB3 |
| [[STAT5A]] | B | STAT5A activity raises LITAF's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.62× lower at baseline in the lines without STAT5A | 0.048 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[NEURL3]] | B | NEURL3 activity raises LITAF's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 2.50× lower at baseline in the lines without NEURL3 | 0.056 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[GBP2]] | B | GBP2 activity raises LITAF's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 1.81× lower at baseline in the lines without GBP2 | 0.057 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[RHBDL2]] | B | RHBDL2 activity raises LITAF's level | lines that do not express RHBDL2 (22) vs lines expressing it (28) | 1.83× lower at baseline in the lines without RHBDL2 | 0.062 | ⚠ within organs, on part of the lines; also absent: AFAP1-AS1, CFB, GPX3; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM | C | LITAF activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express LITAF (3) vs lines expressing it (45) | the lines without LITAF: 0.65× the cells of the other lines | 0.008 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KIAA1522, SKAP2 |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | C | LITAF activity raises the cells' numbers under Idarubicin (hydrochloride) 0.5 µM (protects the cells) | lines that do not express LITAF (3) vs lines expressing it (45) | the lines without LITAF: 0.52× the cells of the other lines | 0.018 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KIAA1522, SKAP2 |
| cells under [[Infigratinib (drug)]] 5 µM | C | LITAF activity raises the cells' numbers under Infigratinib 5 µM (protects the cells) | lines that do not express LITAF (3) vs lines expressing it (45) | the lines without LITAF: 0.58× the cells of the other lines | 0.045 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KIAA1522, SKAP2 |
| cells under [[Trametinib (drug)]] 5 µM | C | LITAF activity raises the cells' numbers under Trametinib 5 µM (protects the cells) | lines that do not express LITAF (3) vs lines expressing it (45) | the lines without LITAF: 0.64× the cells of the other lines | 0.075 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KIAA1522, SKAP2 |
| cells under [[Selinexor (drug)]] 0.5 µM | C | LITAF activity raises the cells' numbers under Selinexor 0.5 µM (protects the cells) | lines that do not express LITAF (3) vs lines expressing it (45) | the lines without LITAF: 0.74× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: SAT1, KIAA1522, SKAP2 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.666). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.2, 2.0); signed map (47.3, 11.3). **Vector** length 122, 36.1% of its response variance represented; |z| ≥ 3 in 1,129 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +9.6 | +15.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +12.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +10.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.8 | +0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.7 | +2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.7 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +8.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -6.4 | -12.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.3 | -12.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.4 | -9.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.3 | -0.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.3 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -1.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | lipopolysaccharide induced TNF factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.13 — chr16:11,547,722-11,636,381 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PIG7, SIMPLE, FLJ38636, TP53I7 |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99732](https://www.uniprot.org/uniprotkb/Q99732) (Lipopolysaccharide-induced tumor necrosis factor-alpha factor):

> Plays a role in endosomal protein trafficking and in targeting proteins for lysosomal degradation. Plays a role in targeting endocytosed EGFR and ERGG3 for lysosomal degradation, and thereby helps down-regulate downstream signaling cascades. Helps recruit the ESCRT complex components TSG101, HGS and STAM to cytoplasmic membranes. Probably plays a role in regulating protein degradation via its interaction with NEDD4. May also contribute to the regulation of gene expression in the nucleus. Binds …

**Summary**, from NCBI Gene [9516](https://www.ncbi.nlm.nih.gov/gene/9516):

> Lipopolysaccharide is a potent stimulator of monocytes and macrophages, causing secretion of tumor necrosis factor-alpha (TNF-alpha) and other inflammatory mediators. This gene encodes lipopolysaccharide-induced TNF-alpha factor, which is a DNA-binding protein and can mediate the TNF-alpha expression by direct binding to the promoter region of the TNF-alpha gene. The transcription of this gene is induced by tumor suppressor p53 and has been implicated in the p53-induced apoptotic pathway. …

**Accessions** — [HGNC:16841](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16841) · Entrez [9516](https://www.ncbi.nlm.nih.gov/gene/9516) · UniProt [Q99732](https://www.uniprot.org/uniprotkb/Q99732) · Ensembl [ENSG00000189067](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189067)

## Data

Gene col 12086: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12086); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12086, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12086]; `tensor/DDL_lfc|DDL_z.npy` [12086]; `embed/gene_vectors.npy` [12086]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12086 or target_col == 12086). Every well: [[LITAF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LITAF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
