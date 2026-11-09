---
symbol: "PAG1"
type: "gene"
col: 1157
ensembl_id: "ENSG00000076641"
name: "phosphoprotein membrane anchor with glycosphingolipid microdomains 1"
location: "8q21.13"
module: 106
arm: "+"
pooled_cpm: 121.76
n_lines_expressing: 35
n_dd_up: 12
n_dd_down: 31
n_dd_up_clean: 11
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 9
direction_downstream: 12
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# PAG1

*phosphoprotein membrane anchor with glycosphingolipid microdomains 1* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.91× (z +19.5, q 0e+00, up in 27 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.334× (z -32.9, q 0e+00, down in 34 of 34 measured lines).
> Its strongest partners by |cos| (84 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKP2]] (+0.58, fdr 4e-05), [[JARID2]] (+0.57, fdr 2e-05), [[PADI2]] (+0.56, fdr 1e-04); moves opposite to [[MAPKAPK5]] (-0.57, fdr 5e-05), [[PBLD]] (-0.54, fdr 5e-04), [[METTL4]] (-0.53, fdr 3e-04).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CA12]] → it (grade B ⚠); 12 go from it, the strongest it → [[ATP2B1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1157.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +19.5 | 0e+00 | 27/33 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.26×** | +17.4 | 0e+00 | 26/33 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.20×** | +16.8 | 0e+00 | 27/33 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.05×** | +15.2 | 0e+00 | 26/33 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +11.5 | 2e-28 | 22/33 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +10.0 | 1e-21 | 22/34 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.82×** | +6.7 | 2e-09 | 19/33 (SHP-77, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.75×** | +6.2 | 3e-08 | 18/34 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.60×** | +5.2 | 1e-05 | 14/33 (SW480, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.22×** | +4.2 | 0.001 | 13/33 (C32, NCI-H1792, …) | rises with dose |  |
| [[Cytarabine (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.002 | 6/33 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.20×** | +3.9 | 0.004 | 8/35 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.007 | 10/33 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Bexarotene (drug)]] 5 µM |  | 1.18× | +3.6 | 0.015 | 8/33 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.029 | 7/33 (SNU-423, LS 180, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | 1.17× | +3.3 | 0.035 | 9/33 (NCI-H460, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1157.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.334×** | -32.9 | 0e+00 | 34/34 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.431×** | -16.6 | 0e+00 | 23/30 (SNU-423, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.523×** | -13.7 | 1e-40 | 23/34 (SNU-423, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.558×** | -11.5 | 1e-28 | 27/33 (hTERT-HPNE, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.626×** | -9.2 | 3e-18 | 24/32 (HS-578T, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.635×** | -8.9 | 5e-17 | 22/31 (hTERT-HPNE, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.675×** | -8.3 | 6e-15 | 21/33 (LoVo, HT-29, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.757×** | -8.3 | 6e-15 | 21/33 (CFPAC-1, SW 900, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.690×** | -7.9 | 3e-13 | 22/33 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.702×** | -7.5 | 4e-12 | 23/33 (HT-29, LoVo, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.685×** | -7.5 | 4e-12 | 23/35 (hTERT-HPNE, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.790×** | -7.0 | 1e-10 | 23/33 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.704×** | -6.9 | 2e-10 | 21/32 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.760×** | -5.8 | 3e-07 | 15/32 (SNU-423, NCI-H460, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.750×** | -5.7 | 4e-07 | 22/33 (LoVo, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.770×** | -5.5 | 1e-06 | 16/33 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.627×** | -5.2 | 7e-06 | 16/33 (LoVo, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **0.794×** | -4.8 | 4e-05 | 15/34 (LoVo, A498, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.769×** | -4.8 | 4e-05 | 17/33 (NCI-H460, NCI-H2347, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.806×** | -4.6 | 1e-04 | 18/33 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1157. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 418 | 0 | 18 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -39.9) |
| [[HOP62 (line)]] | alt | 263 | 0 | 14 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -21.0) |
| [[SNU-423 (line)]] | alt | 295 | 0 | 14 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0540× (z -31.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.149× (z -31.5) |
| [[hTERT-HPNE (line)]] | wt | 335 | 4 (3 ⚠) | 9 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +10.6) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 1.75× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -28.7) |
| [[RPMI-7951 (line)]] | alt | 349 | 0 | 12 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.125× (z -32.9) |
| [[C32 (line)]] | wt | 114 | 9 (4 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +18.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.45× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -12.8) |
| [[HS-578T (line)]] | alt | 270 | 1 | 9 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.26× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.171× (z -28.2) |
| [[NCI-H460 (line)]] | wt | 310 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -34.4) |
| [[NCI-H1792 (line)]] | alt | 223 | 0 | 8 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -26.0) |
| [[NCI-H2030 (line)]] | alt | 110 | 4 | 4 | [[Panobinostat (drug)]] 5 µM 4.57× (z +16.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -19.8) |
| [[SW 900 (line)]] | alt | 319 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -23.2) |
| [[SW480 (line)]] | alt | 31.4 | 7 (1 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.59× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -13.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 126 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -23.3) |
| [[NCI-H2347 (line)]] | alt | 239 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -18.1) |
| [[A498 (line)]] | wt | 194 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.47× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -15.2) |
| [[KATO III (line)]] | alt | 87.3 | 4 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.66× (z +15.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.349× (z -16.7) |
| [[LS 180 (line)]] | wt | 155 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -16.7) |
| [[NCI-H1573 (line)]] | alt | 54.3 | 1 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.91× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -12.2) |
| [[BT-474 (line)]] | alt | 41.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.22× (z +15.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 3.37× (z +11.5) | — |
| [[J82 (line)]] | alt | 167 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -15.0) |
| [[SK-MEL-2 (line)]] | alt | 34.2 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.46× (z +14.4) | — |
| [[AsPC-1 (line)]] | alt | 169 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -17.3) |
| [[CFPAC-1 (line)]] | alt | 70.0 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -16.8) |
| [[HEC-1-A (line)]] | alt | 31.4 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 4.25× (z +16.2) | — |
| [[SHP-77 (line)]] | alt | 31.6 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 3.57× (z +10.7) | — |
| [[H4 (line)]] | wt | 42.4 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 5.29× (z +10.2) | [[Hydroxyurea (drug)]] 0.05 µM 0.207× (z -8.9) |
| [[Panc 03.27 (line)]] | alt | 57.1 | 2 | 1 | [[Tucidinostat (drug)]] 5 µM 2.64× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -14.8) |
| [[SW 1088 (line)]] | alt | 339 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -12.7) |
| [[CHP-212 (line)]] | wt | 53.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -8.7) |
| [[SW 1271 (line)]] | alt | 164 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -11.7) |
| [[SW48 (line)]] | wt | 44.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 28.9 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 8.41 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 18.4 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 20.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 19.4 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 25.2 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 23.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.24 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 13.8 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 13.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1157), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKP2]] | +0.58 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[JARID2]] | +0.57 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[PADI2]] | +0.56 | +0.37 / +0.35 | both halves | 1e-04 |  |
| [[RNF24]] | +0.56 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[RIC1]] | +0.55 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[DEPP1]] | +0.55 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[MARCHF3]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[UGCG]] | +0.55 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[CCDC88A]] | +0.54 | +0.39 / +0.36 | both halves | 1e-04 |  |
| [[ESYT2]] | +0.54 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[SLC2A13]] | +0.54 | +0.52 / +0.36 | both halves | 1e-04 |  |
| [[PIGH]] | +0.53 | +0.39 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 14 of them with an alert (⚠; 14 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPKAPK5]] | -0.57 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[PBLD]] | -0.54 | -0.37 / -0.23 | both halves | 5e-04 |  |
| [[METTL4]] | -0.53 | -0.29 / -0.35 | both halves | 3e-04 |  |
| [[ZCWPW1]] | -0.53 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[GABPB1]] | -0.53 | -0.41 / -0.29 | both halves | 3e-04 |  |
| [[RCC1L]] | -0.52 | -0.34 / -0.38 | both halves | 1e-04 |  |
| [[AP5M1]] | -0.52 | -0.42 / -0.15 | ⚠ not reproduced | 0.001 |  |
| [[VPS52]] | -0.52 | -0.35 / -0.29 | both halves | 2e-04 |  |
| [[ANGEL2]] | -0.52 | -0.35 / -0.23 | both halves | 5e-04 |  |
| [[ZNF362]] | -0.52 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[KMT2D]] | -0.51 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[LINC01134]] | -0.51 | -0.22 / -0.21 | both halves | 6e-04 |  |
| [[TOR1A]] | -0.50 | -0.26 / -0.34 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CA12]] | B | CA12 activity raises PAG1's level | lines that do not express CA12 (29) vs lines expressing it (21) | 3.15× lower at baseline in the lines without CA12 | 0.013 | ⚠ within organs, on part of the lines; also absent: NID2, IL33, IDO1 |
| [[NEDD9]] | B | NEDD9 activity raises PAG1's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 3.21× lower at baseline in the lines without NEDD9 | 0.040 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[RGS2]] | B | RGS2 activity raises PAG1's level | lines that do not express RGS2 (17) vs lines expressing it (33) | 2.91× lower at baseline in the lines without RGS2 | 0.049 | ⚠ within organs, on part of the lines; also absent: LINC01393, P2RY1, MEF2C-AS1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises PAG1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00698]] | B | LINC00698 activity raises PAG1's level | lines that do not express LINC00698 (30) vs lines expressing it (20) | 1.76× lower at baseline in the lines without LINC00698 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000253642, HEPH, SRRM4; maybe low, not absent |
| [[CGAS]] | B | CGAS activity weakens PAG1's drug response | lines that do not express CGAS (11) vs lines expressing it (23) | the lines without CGAS respond 1.09× as strongly (z diff -0.38); strongest at Tucidinostat 5 µM: 2.56x vs 1.50x (z diff -3.6) | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000234902, C15orf48, TYMP; target measured in part of the lines; both ways; artifact flags |
| [[PTPRM]] | B | PTPRM activity raises PAG1's level | lines that do not express PTPRM (18) vs lines expressing it (32) | 2.90× lower at baseline in the lines without PTPRM | 0.087 | ⚠ within organs, on part of the lines; also absent: FIGN, MAP9, CCDC169 |
| [[FRY]] | B | FRY activity raises PAG1's level | lines that do not express FRY (14) vs lines expressing it (36) | 2.38× lower at baseline in the lines without FRY | 0.087 | ⚠ within organs, on part of the lines; also absent: ADGRV1, DTNA, ZNF385B |
| [[FLNB]] | C | FLNB activity raises PAG1's level | lines that do not express FLNB (3) vs lines expressing it (47) | 4.55× lower at baseline in the lines without FLNB | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MYO1E, B4GALT1, SMOX; maybe low, not absent; its own permutation p |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP2B1]] | B | PAG1 activity raises ATP2B1's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 2.09× lower at baseline in the lines without PAG1 | 0.009 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| [[ANGEL2]] | B | PAG1 activity lowers ANGEL2's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 1.33× higher at baseline in the lines without PAG1 | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| [[ANKRD18B]] | B | PAG1 activity strengthens ANKRD18B's drug response | lines that do not express PAG1 (7) vs lines expressing it (18) | the lines without PAG1 respond 0.73× as strongly (z diff +1.66); strongest at Epirubicin (hydrochloride) 5 µM: 1.14x vs 2.36x (z diff +3.6) | 0.016 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3; target measured in part of the lines; artifact flags |
| [[ESYT2]] | B | PAG1 activity raises ESYT2's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 1.47× lower at baseline in the lines without PAG1 | 0.037 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| [[JARID2]] | B | PAG1 activity raises JARID2's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 1.77× lower at baseline in the lines without PAG1 | 0.039 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| [[NDRG1]] | B | PAG1 activity raises NDRG1's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 2.47× lower at baseline in the lines without PAG1 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| [[STK17B]] | B | PAG1 activity raises STK17B's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 1.65× lower at baseline in the lines without PAG1 | 0.059 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| [[AKAP13]] | B | PAG1 activity raises AKAP13's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 1.36× lower at baseline in the lines without PAG1 | 0.067 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| [[FAM13A]] | B | PAG1 activity raises FAM13A's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 2.13× lower at baseline in the lines without PAG1 | 0.073 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| [[FRY]] | B | PAG1 activity raises FRY's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without PAG1 | 0.087 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| cells under [[Cysteamine (hydrochloride) (drug)]] 5 µM | B | PAG1 activity raises the cells' numbers under Cysteamine (hydrochloride) 5 µM (protects the cells) | lines that do not express PAG1 (15) vs lines expressing it (33) | the lines without PAG1: 0.91× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| [[ESYT2]] | B | PAG1 activity strengthens ESYT2's drug response | lines that do not express PAG1 (15) vs lines expressing it (34) | the lines without PAG1 respond 0.67× as strongly (z diff +2.17); strongest at Idarubicin (hydrochloride) 5 µM: 0.70x vs 0.53x (z diff +3.0) | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.382). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.5, -10.9); signed map (-27.2, 28.7). **Vector** length 124, 34.7% of its response variance represented; |z| ≥ 3 in 1,366 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +19.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.4 | +15.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.4 | +17.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +7.3 | +16.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.9 | +11.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +6.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.5 | +6.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +5.2 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.1 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -32.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -11.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.3 | -8.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.0 | -9.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -7.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.1 | -7.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -8.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.0 | -4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.0 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphoprotein membrane anchor with glycosphingolipid microdomains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:80,967,810-81,112,068 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAG, CBP |
| Reactome | 6 pathways, smallest: Phosphorylation of CD3 and TCR zeta chains; GAB1 signalosome; Signaling by EGFR |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWQ8](https://www.uniprot.org/uniprotkb/Q9NWQ8) (Phosphoprotein associated with glycosphingolipid-enriched microdomains 1):

> Negatively regulates TCR (T-cell antigen receptor)-mediated signaling in T-cells and FCER1 (high affinity immunoglobulin epsilon receptor)-mediated signaling in mast cells. Promotes CSK activation and recruitment to lipid rafts, which results in LCK inhibition. Inhibits immunological synapse formation by preventing dynamic arrangement of lipid raft proteins. May be involved in cell adhesion signaling.

**Summary**, from NCBI Gene [55824](https://www.ncbi.nlm.nih.gov/gene/55824):

> The protein encoded by this gene is a type III transmembrane adaptor protein that binds to the tyrosine kinase csk protein. It is thought to be involved in the regulation of T cell activation. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:30043](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30043) · Entrez [55824](https://www.ncbi.nlm.nih.gov/gene/55824) · UniProt [Q9NWQ8](https://www.uniprot.org/uniprotkb/Q9NWQ8) · Ensembl [ENSG00000076641](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076641)

## Data

Gene col 1157: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1157); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1157, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1157]; `tensor/DDL_lfc|DDL_z.npy` [1157]; `embed/gene_vectors.npy` [1157]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1157 or target_col == 1157). Every well: [[PAG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
