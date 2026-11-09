---
symbol: "PDS5A"
type: "gene"
col: 4301
ensembl_id: "ENSG00000121892"
name: "PDS5 cohesin associated factor A"
location: "4p14"
module: 18
arm: "+"
pooled_cpm: 250.6
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 5
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# PDS5A

*PDS5 cohesin associated factor A* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.34× (z +8.8, q 8e-16, up in 40 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.30× (z +8.1, q 1e-13, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.533× (z -19.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPECC1L]] (+0.63, fdr 4e-05), [[NAE1]] (+0.62, fdr 8e-06), [[TRRAP]] (+0.62, fdr 7e-06); moves opposite to [[NFKBIE]] (-0.63, fdr 1e-05), [[NR1D1]] (-0.61, fdr 8e-06), [[CCDC148]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ERC1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4301.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +8.8 | 8e-16 | 40/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +8.1 | 1e-13 | 31/48 (HCT15, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +7.9 | 6e-13 | 28/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +6.6 | 6e-09 | 30/48 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +6.3 | 3e-08 | 25/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +6.1 | 1e-07 | 27/48 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +5.8 | 5e-07 | 24/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.18× | +5.1 | 3e-05 | 21/48 (HCT15, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | 1.16× | +4.3 | 0.001 | 19/48 (Hs 766T, HT-29, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.14× | +4.1 | 0.003 | 7/48 (CFPAC-1, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.11× | +3.3 | 0.052 | 14/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 1.12× | +3.3 | 0.052 | 2/48 (SW1417, NCI-H2030) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.062 | 15/49 (RKO, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4301.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.533×** | -19.4 | 0e+00 | 47/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.659×** | -18.2 | 0e+00 | 39/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.584×** | -16.6 | 0e+00 | 44/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.588×** | -16.4 | 0e+00 | 46/48 (SW480, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -14.7 | 0e+00 | 38/49 (NCI-H2030, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.708×** | -10.6 | 3e-24 | 32/48 (NCI-H1573, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.730×** | -9.7 | 2e-20 | 38/48 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.745×** | -8.7 | 2e-16 | 37/47 (A-427, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.754×** | -8.4 | 3e-15 | 32/50 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.829×** | -8.2 | 1e-14 | 25/48 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.857× | -6.7 | 8e-10 | 20/48 (A-427, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.804×** | -6.7 | 8e-10 | 28/48 (SW480, NCI-H2030, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.813×** | -6.1 | 3e-08 | 26/48 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.814×** | -6.1 | 4e-08 | 26/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **0.827×** | -5.9 | 2e-07 | 27/48 (HOP62, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.863× | -4.5 | 2e-04 | 12/49 (NCI-H2347, A-427, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.814×** | -4.2 | 9e-04 | 28/47 (MIA PaCa-2, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.766×** | -3.2 | 0.034 | 19/49 (J82, NCI-H2030, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.860× | -3.0 | 0.054 | 10/48 (J82, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.869× | -2.8 | 0.096 | 7/49 (LoVo, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4301. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 319 | 5 (2 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.15× (z +16.0) | [[Panobinostat (drug)]] 0.5 µM 0.447× (z -16.9) |
| [[NCI-H460 (line)]] | wt | 259 | 0 | 9 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -18.8) |
| [[NCI-H2030 (line)]] | alt | 335 | 0 | 8 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -25.0) |
| [[C-33 A (line)]] | alt | 343 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -13.6) |
| [[LS 180 (line)]] | wt | 288 | 3 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.99× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.420× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.467× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 277 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -28.6) |
| [[NCI-H23 (line)]] | alt | 272 | 1 (1 ⚠) | 6 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.68× (z +9.2) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -26.8) |
| [[A-172 (line)]] | wt | 198 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -13.0) |
| [[A-427 (line)]] | wt | 324 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.469× (z -15.7) |
| [[A498 (line)]] | wt | 235 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -16.7) |
| [[HOP62 (line)]] | alt | 259 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -26.8) |
| [[J82 (line)]] | alt | 219 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.543× (z -16.4) |
| [[MIA PaCa-2 (line)]] | alt | 260 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.402× (z -17.4) |
| [[SW 900 (line)]] | alt | 397 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -14.3) |
| [[SW480 (line)]] | alt | 251 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.451× (z -18.6) |
| [[C32 (line)]] | wt | 201 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.541× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 271 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -21.4) |
| [[PANC-1 (line)]] | alt | 221 | 1 (1 ⚠) | 4 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.51× (z +9.2) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -16.1) |
| [[RKO (line)]] | wt | 378 | 1 | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.67× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -15.6) |
| [[SK-MEL-2 (line)]] | alt | 232 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.500× (z -12.2) |
| [[SNU-1 (line)]] | wt | 349 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.550× (z -12.7) |
| [[SW1417 (line)]] | alt | 208 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.445× (z -15.6) |
| [[A549 (line)]] | wt | 203 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -20.2) |
| [[AsPC-1 (line)]] | alt | 271 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.417× (z -13.7) |
| [[BT-474 (line)]] | alt | 236 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.341× (z -16.6) |
| [[KATO III (line)]] | alt | 242 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.74× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.510× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 200 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -21.3) |
| [[SNU-423 (line)]] | alt | 227 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.476× (z -11.9) |
| [[SW48 (line)]] | wt | 355 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.421× (z -12.7) |
| [[HCT15 (line)]] | alt | 350 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -14.4) |
| [[HEC-1-A (line)]] | alt | 250 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.601× (z -11.2) |
| [[HepG2_C3A (line)]] | wt | 239 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.430× (z -11.4) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.469× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 216 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -18.4) |
| [[NCI-H2347 (line)]] | alt | 287 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.444× (z -15.3) |
| [[Panc 03.27 (line)]] | alt | 212 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.510× (z -11.7) |
| [[AN3 CA (line)]] | alt | 341 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 182 | 1 | 1 | [[Vinblastine (sulfate) (drug)]] 5 µM 1.50× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.584× (z -11.8) |
| [[COLO 205 (line)]] | alt | 176 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.22× (z +10.6) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -12.8) |
| [[Hs 766T (line)]] | wt | 197 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 1.74× (z +8.5) ⚠ toxic | [[Panobinostat (drug)]] 0.5 µM 0.578× (z -8.6) |
| [[SW 1271 (line)]] | alt | 285 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.6) |
| [[CHP-212 (line)]] | wt | 246 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -11.4) |
| [[H4 (line)]] | wt | 242 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.485× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[HS-578T (line)]] | alt | 177 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -17.6) |
| [[RPMI-7951 (line)]] | alt | 171 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.564× (z -10.6) |
| [[SHP-77 (line)]] | alt | 121 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.97× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | — |
| [[SW 1088 (line)]] | alt | 140 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.0842× (z -10.8) |
| [[HT-29 (line)]] | alt | 227 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 390 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4301), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPECC1L]] | +0.63 | +0.70 / +0.41 | both halves | 4e-05 |  |
| [[NAE1]] | +0.62 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[TRRAP]] | +0.62 | +0.64 / +0.65 | both halves | 7e-06 | same gene group |
| [[ECPAS]] | +0.62 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[UBE2K]] | +0.62 | +0.63 / +0.57 | both halves | 1e-05 | STRING 527; ⚠ same locus (40.1 kb: neighbours can correlate without regulation) |
| [[KPNB1]] | +0.61 | +0.67 / +0.54 | both halves | 1e-05 | pathway: Mitotic Anaphase |
| [[RSRC1]] | +0.61 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[HERC2]] | +0.60 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[ZFYVE9]] | +0.60 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[NCKAP1]] | +0.60 | +0.71 / +0.53 | both halves | 1e-05 |  |
| [[LARP1]] | +0.59 | +0.57 / +0.57 | both halves | 9e-06 |  |
| [[KPNA3]] | +0.59 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[ANP32B]] | +0.58 | +0.69 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKBIE]] | -0.63 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[NR1D1]] | -0.61 | -0.58 / -0.59 | both halves | 8e-06 |  |
| [[CCDC148]] | -0.58 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[KDM5B]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[PDGFB]] | -0.56 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[RARA]] | -0.56 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ISG20]] | -0.52 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[GORAB]] | -0.52 | -0.66 / -0.44 | both halves | 3e-05 |  |
| [[HLA-A]] | -0.52 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[KLHL28]] | -0.51 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ACAP1]] | -0.51 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[DBP]] | -0.51 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PDS5A's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERC1]] | C | PDS5A's natural level strengthens ERC1's drug response | PDS5A's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.64, reverse +0.38; direction not clear | 0.056 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.642). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.5, -33.5); signed map (-17.9, -50.8). **Vector** length 112, 37.1% of its response variance represented; |z| ≥ 3 in 1,353 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.0 | +6.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.7 | +8.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.9 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | +5.8 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | +5.4 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +5.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.9 | +1.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | +0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.0 | +4.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.9 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.8 | -18.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.8 | -10.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | -1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.1 | -6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -4.1 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.8 | -8.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.7 | -2.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.3 | -3.0 |
|  | [[Pimitespib (drug)]] 5 µM |  | -2.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | PDS5 cohesin associated factor A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:39,822,863-39,977,956 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0648, PIG54, SCC-112 |
| Gene groups (HGNC) | Armadillo like helical domain containing |
| Reactome | 12 pathways, smallest: Cohesin Loading onto Chromatin; Establishment of Sister Chromatid Cohesion; Mitotic Telophase/Cytokinesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q29RF7](https://www.uniprot.org/uniprotkb/Q29RF7) (Sister chromatid cohesion protein PDS5 homolog A):

> Probable regulator of sister chromatid cohesion in mitosis which may stabilize cohesin complex association with chromatin. May couple sister chromatid cohesion during mitosis to DNA replication. Cohesion ensures that chromosome partitioning is accurate in both meiotic and mitotic cells and plays an important role in DNA repair.

**Summary**, from NCBI Gene [23244](https://www.ncbi.nlm.nih.gov/gene/23244):

> The protein encoded by this gene binds to the cohesin complex and associates with chromatin through most of the cell cycle. The encoded protein may play a role in regulating sister chromatid cohesion during mitosis. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:29088](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29088) · Entrez [23244](https://www.ncbi.nlm.nih.gov/gene/23244) · UniProt [Q29RF7](https://www.uniprot.org/uniprotkb/Q29RF7) · Ensembl [ENSG00000121892](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121892)

## Data

Gene col 4301: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4301); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4301, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4301]; `tensor/DDL_lfc|DDL_z.npy` [4301]; `embed/gene_vectors.npy` [4301]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4301 or target_col == 4301). Every well: [[PDS5A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDS5A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
