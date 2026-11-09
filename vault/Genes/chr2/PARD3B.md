---
symbol: "PARD3B"
type: "gene"
col: 3760
ensembl_id: "ENSG00000116117"
name: "par-3 family cell polarity regulator beta"
location: "2q33.3"
module: 143
arm: "+"
pooled_cpm: 115.99
n_lines_expressing: 41
n_dd_up: 27
n_dd_down: 26
n_dd_up_clean: 26
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/143"]
generated_by: "tahoemap"
---

# PARD3B

*par-3 family cell polarity regulator beta* — 2q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.56× (z +5.2, q 9e-05, up in 30 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.341× (z -13.1, q 2e-36, down in 35 of 39 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.346× (z -12.9, q 1e-35, down in 36 of 39 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R9A]] (+0.80, fdr 7e-06), [[GRIP1]] (+0.70, fdr 7e-06), [[IQCH-AS1]] (+0.69, fdr 1e-05); moves opposite to [[SWI5]] (-0.64, fdr 3e-05), [[VRK3]] (-0.63, fdr 1e-05), [[SDF2]] (-0.61, fdr 1e-05).
> It is in [[Module 143]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TLCD4-RWDD3]] → it (grade B ⚠); 4 go from it, the strongest it → [[TLCD4-RWDD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3760.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.56×** | +5.2 | 9e-05 | 30/38 (LoVo, HCT15, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.52×** | +5.1 | 9e-05 | 29/39 (LoVo, KATO III, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.6 | 8e-04 | 21/38 (NCI-H1792, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +4.3 | 0.002 | 22/39 (NCI-H2347, SNU-1, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +4.1 | 0.005 | 21/39 (LoVo, NCI-H23, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.011 | 21/38 (LoVo, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.011 | 22/39 (NCI-H23, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.34×** | +3.6 | 0.024 | 25/39 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +3.5 | 0.029 | 19/39 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.029 | 22/39 (C32, J82, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.031 | 17/39 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.031 | 20/39 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.032 | 18/38 (LoVo, A-172, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.38×** | +3.4 | 0.032 | 20/41 (LoVo, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.22×** | +3.3 | 0.035 | 19/40 (SW480, HCT15, …) | all doses, flat |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.68×** | +3.3 | 0.035 | 19/41 (LoVo, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3760.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.341×** | -13.1 | 2e-36 | 35/39 (LS 180, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.346×** | -12.9 | 1e-35 | 36/39 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.362×** | -11.9 | 2e-30 | 32/38 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.406×** | -11.0 | 9e-26 | 34/39 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.447×** | -9.8 | 1e-20 | 28/38 (NCI-H460, SW48, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.489×** | -8.7 | 3e-16 | 26/39 (SW48, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.505×** | -8.3 | 6e-15 | 35/39 (A-427, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.505×** | -8.3 | 6e-15 | 33/39 (SW48, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.521×** | -7.9 | 1e-13 | 26/39 (RKO, C-33 A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.584×** | -6.6 | 3e-09 | 31/39 (A-427, C-33 A, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.390×** | -6.0 | 1e-07 | 26/40 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.621×** | -5.8 | 3e-07 | 27/39 (SW48, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.628×** | -5.7 | 6e-07 | 23/39 (RKO, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.651×** | -4.9 | 3e-05 | 24/39 (SW1417, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.505×** | -4.4 | 5e-04 | 24/39 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.003 | 25/40 (A-172, Panc 03.27, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -3.7 | 0.008 | 22/39 (LoVo, LS 180, …) | top dose only | plate-row cell shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.742×** | -3.5 | 0.013 | 21/39 (SNU-423, HT-29, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.686×** | -3.5 | 0.013 | 22/39 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.745×** | -3.3 | 0.022 | 21/38 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.686×** | -3.3 | 0.025 | 19/39 (LoVo, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.600×** | -3.3 | 0.026 | 22/39 (C-33 A, NCI-H23, …) | rises with dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3760. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 349 | 0 | 13 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.103× (z -19.2) |
| [[LoVo (line)]] | wt | 417 | 3 (1 ⚠) | 9 (6 ⚠) | [[Trametinib (drug)]] 5 µM 2.01× (z +8.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 2.12× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.123× (z -24.9) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.153× (z -22.4) |
| [[NCI-H460 (line)]] | wt | 72.4 | 0 | 12 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.446× (z -10.5) |
| [[LS 180 (line)]] | wt | 448 | 0 | 10 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.104× (z -24.3) |
| [[RKO (line)]] | wt | 138 | 0 | 10 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.223× (z -10.7) |
| [[SNU-1 (line)]] | wt | 225 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.198× (z -12.8) |
| [[SW1417 (line)]] | alt | 302 | 0 | 9 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.223× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.242× (z -13.6) |
| [[A-427 (line)]] | wt | 153 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -13.6) |
| [[C-33 A (line)]] | alt | 183 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.167× (z -15.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.189× (z -14.5) |
| [[SW480 (line)]] | alt | 82.1 | 0 | 8 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.183× (z -13.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.189× (z -13.5) |
| [[HT-29 (line)]] | alt | 135 | 0 | 7 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.179× (z -12.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.240× (z -10.4) |
| [[HCT15 (line)]] | alt | 205 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.204× (z -12.0) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.271× (z -10.2) |
| [[KATO III (line)]] | alt | 135 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.132× (z -18.7) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.140× (z -18.1) |
| [[NCI-H23 (line)]] | alt | 67.8 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +19.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.145× (z -14.2) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.256× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 256 | 0 | 5 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.223× (z -11.3) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.303× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 278 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.201× (z -19.3) |
| [[A549 (line)]] | wt | 72.5 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.224× (z -10.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.266× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 96.2 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.303× (z -10.2) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 65.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +17.2) | — |
| [[AN3 CA (line)]] | alt | 171 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.146× (z -11.1) ⚠ cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 71.5 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.295× (z -9.6) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.341× (z -8.5) |
| [[SNU-423 (line)]] | alt | 108 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.280× (z -9.7) |
| [[A498 (line)]] | wt | 50.2 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.287× (z -9.0) ⚠ cell-cycle shift, explains ~25% of this change |
| [[BT-474 (line)]] | alt | 121 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -10.7) |
| [[C32 (line)]] | wt | 191 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.277× (z -9.6) |
| [[J82 (line)]] | alt | 228 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.248× (z -11.3) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 56.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -8.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[NCI-H661 (line)]] | alt | 736 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -9.1) ⚠ cell-cycle shift, explains ~89% of this change |
| [[A-172 (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 21.1 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 65.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 56.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.6 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.5 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3760), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R9A]] | +0.80 | +0.76 / +0.78 | both halves | 7e-06 | same gene group |
| [[GRIP1]] | +0.70 | +0.74 / +0.58 | both halves | 7e-06 | same gene group |
| [[IQCH-AS1]] | +0.69 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[FBXL17]] | +0.69 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[ADGRA3]] | +0.67 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[PHACTR2]] | +0.66 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[PTPRK]] | +0.66 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[TCF12]] | +0.64 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NFIB]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[PLCB4]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[SLC12A2-DT]] | +0.61 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[TENM3]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SWI5]] | -0.64 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[VRK3]] | -0.63 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[SDF2]] | -0.61 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[SDHAP1]] | -0.61 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[OGG1]] | -0.60 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[HSPB11]] | -0.60 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[ATAT1]] | -0.60 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[GIPR]] | -0.58 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[LCMT1]] | -0.58 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[RNF121]] | -0.56 | -0.59 / -0.38 | both halves | 7e-05 |  |
| [[FCHSD1]] | -0.56 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[PCTP]] | -0.56 | -0.59 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLCD4-RWDD3]] | B | TLCD4-RWDD3 activity raises PARD3B's level | lines that do not express TLCD4-RWDD3 (11) vs lines expressing it (39) | 3.94× lower at baseline in the lines without TLCD4-RWDD3 | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SLC16A9, ALDH5A1, NUP210; maybe low, not absent |
| [[ARHGEF28]] | B | ARHGEF28 activity lowers PARD3B's level | lines that do not express ARHGEF28 (6) vs lines expressing it (44) | 3.28× higher at baseline in the lines without ARHGEF28 | 0.039 | ⚠ within organs, on part of the lines; also absent: SHB, RABGEF1P3, TBILA; maybe low, not absent |
| [[DPH6-DT]] | C | DPH6-DT activity raises PARD3B's level | lines that do not express DPH6-DT (3) vs lines expressing it (47) | 7.36× lower at baseline in the lines without DPH6-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MINDY4, MYO10, SPDL1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLCD4-RWDD3]] | B | PARD3B activity raises TLCD4-RWDD3's level | lines that do not express PARD3B (9) vs lines expressing it (41) | 1.88× lower at baseline in the lines without PARD3B | 0.048 | ⚠ within organs, on part of the lines; also absent: MRAS, LPCAT2, ZNF618 |
| [[TENM3]] | B | PARD3B activity raises TENM3's level | lines that do not express PARD3B (9) vs lines expressing it (41) | 4.52× lower at baseline in the lines without PARD3B | 0.074 | ⚠ within organs, on part of the lines; also absent: MRAS, LPCAT2, ZNF618 |
| [[GPR89B]] | B | PARD3B activity lowers GPR89B's level | lines that do not express PARD3B (9) vs lines expressing it (41) | 1.12× higher at baseline in the lines without PARD3B | 0.089 | ⚠ within organs, on part of the lines; also absent: MRAS, LPCAT2, ZNF618 |
| [[FRG1-DT]] | B | PARD3B activity lowers FRG1-DT's level | lines that do not express PARD3B (9) vs lines expressing it (41) | 1.10× higher at baseline in the lines without PARD3B | 0.098 | ⚠ within organs, on part of the lines; also absent: MRAS, LPCAT2, ZNF618 |

## Where it sits

- **Module**: [[Module 143]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.799). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.7, 7.6); signed map (24.6, -32.0). **Vector** length 121, 39.9% of its response variance represented; |z| ≥ 3 in 1,198 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.4 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +6.1 | +4.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +5.3 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +5.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.6 | -11.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -5.4 | -13.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -12.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.7 | -6.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.1 | -11.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.6 | -3.3 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.4 | -2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -0.1 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.2 | -0.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | par-3 family cell polarity regulator beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.3 — chr2:204,545,475-205,620,162 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Par3L, PAR3beta; previously ALS2CR19 |
| Gene groups (HGNC) | PDZ domain containing; Par-3 family cell polarity regulators |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEW8](https://www.uniprot.org/uniprotkb/Q8TEW8) (Partitioning defective 3 homolog B):

> Putative adapter protein involved in asymmetrical cell division and cell polarization processes. May play a role in the formation of epithelial tight junctions.

**Summary**, from NCBI Gene [117583](https://www.ncbi.nlm.nih.gov/gene/117583):

> Predicted to enable phosphatidylinositol binding activity. Predicted to be involved in several processes, including establishment of cell polarity; establishment or maintenance of epithelial cell apical/basal polarity; and microtubule cytoskeleton organization. Located in cell junction. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:14446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14446) · Entrez [117583](https://www.ncbi.nlm.nih.gov/gene/117583) · UniProt [Q8TEW8](https://www.uniprot.org/uniprotkb/Q8TEW8) · Ensembl [ENSG00000116117](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116117)

## Data

Gene col 3760: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3760); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3760, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3760]; `tensor/DDL_lfc|DDL_z.npy` [3760]; `embed/gene_vectors.npy` [3760]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3760 or target_col == 3760). Every well: [[PARD3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARD3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
