---
symbol: "NUF2"
type: "gene"
col: 6702
ensembl_id: "ENSG00000143228"
name: "NUF2 component of NDC80 kinetochore complex"
location: "1q23.3"
module: 67
arm: "+"
pooled_cpm: 53.22
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 26
n_dd_up_clean: 3
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 7
direction_downstream: 1
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# NUF2

*NUF2 component of NDC80 kinetochore complex* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.42× (z +6.8, q 5e-09, up in 27 of 47 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.85× (z +4.2, q 0.002, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.432× (z -11.7, q 8e-29, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TTK]] (+0.93, fdr 7e-06), [[TOP2A]] (+0.90, fdr 7e-06), [[RACGAP1]] (+0.89, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CCP110]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6702.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.42×** | +6.8 | 5e-09 | 27/47 (NCI-H1792, RKO, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.24×** | +5.5 | 1e-05 | 28/47 (A-427, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~66% of this change | **1.49×** | +5.4 | 2e-05 | 25/46 (NCI-H23, C-33 A, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **2.09×** | +5.0 | 8e-05 | 29/46 (J82, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.39×** | +4.6 | 6e-04 | 28/47 (AsPC-1, NCI-H1792, …) | all doses, flat | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.38×** | +4.4 | 8e-04 | 24/46 (A-427, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.36×** | +4.3 | 0.001 | 24/46 (MIA PaCa-2, A-172, …) | two highest doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +4.2 | 0.002 | 23/47 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.22×** | +3.9 | 0.006 | 22/47 (SK-MEL-2, NCI-H1573, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.32×** | +3.9 | 0.006 | 22/47 (NCI-H23, HOP62, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.31×** | +3.6 | 0.014 | 19/40 (KATO III, NCI-H460, …) | two highest doses | composition shift |
| [[Mebendazole (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.024 | 18/47 (SW 900, J82, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.049 | 18/47 (CFPAC-1, RKO, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.064 | 15/47 (SK-MEL-2, NCI-H2347, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +3.1 | 0.083 | 16/46 (NCI-H23, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6702.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.432×** | -11.7 | 8e-29 | 45/47 (HEC-1-A, SW480, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.563×** | -11.3 | 3e-27 | 41/47 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.511×** | -8.8 | 2e-16 | 36/47 (A-172, PANC-1, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.553×** | -8.3 | 2e-14 | 38/47 (A498, A-427, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.663×** | -8.1 | 6e-14 | 36/47 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.595×** | -7.2 | 5e-11 | 42/47 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.704×** | -6.9 | 4e-10 | 33/47 (A-427, A498, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **0.402×** | -6.2 | 4e-08 | 32/43 (A-427, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.685×** | -5.3 | 8e-06 | 25/47 (A-172, A498, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.705×** | -4.9 | 6e-05 | 26/47 (A-172, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.708×** | -4.8 | 8e-05 | 32/47 (Hs 766T, NCI-H460, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.503×** | -4.7 | 1e-04 | 25/47 (SNU-1, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.794×** | -4.6 | 2e-04 | 23/47 (HCT15, MIA PaCa-2, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.729×** | -4.4 | 4e-04 | 27/47 (SNU-1, RKO, …) | rises with dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.740×** | -4.2 | 0.001 | 24/47 (SNU-1, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.813×** | -4.1 | 0.001 | 20/47 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.832×** | -3.6 | 0.008 | 19/47 (A-172, A498, …) | top dose only |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **0.795×** | -3.2 | 0.038 | 13/47 (A549, SK-MEL-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.800×** | -3.1 | 0.047 | 18/47 (SNU-1, A498, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.640×** | -3.0 | 0.057 | 13/47 (HEC-1-A, A498, …) | top dose only | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.862× | -2.9 | 0.073 | 17/47 (HT-29, A-427, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.811×** | -2.9 | 0.073 | 13/46 (RKO, NCI-H2030, …) | two highest doses | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.862× | -2.8 | 0.100 | 16/47 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +1.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6702. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 64.0 | 0 | 8 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.220× (z -16.8) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.374× (z -10.9) |
| [[A498 (line)]] | wt | 55.3 | 0 | 6 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.259× (z -16.7) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.386× (z -11.7) |
| [[LOX-IMVI (line)]] | wt | 59.2 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.112× (z -21.2) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.233× (z -10.0) |
| [[A-427 (line)]] | wt | 92.0 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.268× (z -17.0) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.369× (z -12.9) |
| [[SNU-1 (line)]] | wt | 47.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0704× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.149× (z -9.6) |
| [[H4 (line)]] | wt | 56.4 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.121× (z -14.6) ⚠ cell-cycle shift, explains ~79% of this change |
| [[HOP62 (line)]] | alt | 83.0 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.385× (z -10.5) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -10.1) |
| [[LS 180 (line)]] | wt | 31.7 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.213× (z -12.9) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.317× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 48.4 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +17.6) ⚠ cell-cycle shift, would explain all of this change | [[Auranofin (drug)]] 5 µM 0.289× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 51.4 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.289× (z -13.8) ⚠ cell-cycle shift, explains ~79% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -11.0) |
| [[A549 (line)]] | wt | 49.4 | 0 | 2 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.248× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 61.6 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.337× (z -12.4) |
| [[BT-474 (line)]] | alt | 46.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C32 (line)]] | wt | 42.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.246× (z -13.1) ⚠ cell-cycle shift, explains ~79% of this change |
| [[HS-578T (line)]] | alt | 51.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[hTERT-HPNE (line)]] | wt | 38.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LoVo (line)]] | wt | 22.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.415× (z -8.5) ⚠ cell-cycle shift, explains ~79% of this change |
| [[NCI-H1792 (line)]] | alt | 31.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.0× (z +19.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 75.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +10.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 38.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +12.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 55.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +13.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 47.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +19.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 73.4 | 0 | 1 | — | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM 0.221× (z -8.7) |
| [[SHP-77 (line)]] | alt | 171 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -10.0) |
| [[SNU-423 (line)]] | alt | 40.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.325× (z -8.7) ⚠ cell-cycle shift, explains ~79% of this change |
| [[SW1417 (line)]] | alt | 49.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW48 (line)]] | wt | 47.5 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.189× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 57.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.323× (z -11.5) |
| [[AN3 CA (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 68.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 50.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 75.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 74.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6702), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTK]] | +0.93 | +0.93 / +0.94 | both halves | 7e-06 | STRING 989 |
| [[TOP2A]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | STRING 936 |
| [[RACGAP1]] | +0.89 | +0.86 / +0.89 | both halves | 7e-06 | STRING 783 |
| [[NEK2]] | +0.89 | +0.86 / +0.89 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 952 |
| [[KIF4A]] | +0.89 | +0.89 / +0.87 | both halves | 7e-06 | STRING 911 |
| [[TPX2]] | +0.89 | +0.88 / +0.89 | both halves | 7e-06 | STRING 947 |
| [[CDK1]] | +0.88 | +0.88 / +0.89 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 957 |
| [[DLGAP5]] | +0.88 | +0.87 / +0.88 | both halves | 7e-06 | STRING 964 |
| [[CDCA3]] | +0.88 | +0.86 / +0.87 | both halves | 7e-06 | STRING 844 |
| [[CCNA2]] | +0.88 | +0.88 / +0.87 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 940 |
| [[CIT]] | +0.88 | +0.84 / +0.87 | both halves | 7e-06 | pathway: RHO GTPase Effectors; STRING 552 |
| [[CKAP2]] | +0.87 | +0.86 / +0.85 | both halves | 7e-06 | STRING 767 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises NUF2's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.13× lower at baseline in the lines without PIMREG | 0.024 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises NUF2's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.69× lower at baseline in the lines without NDC80 | 0.019 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises NUF2's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.54× lower at baseline in the lines without AURKB | 0.032 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises NUF2's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.81× lower at baseline in the lines without PBK | 0.035 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises NUF2's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.17× lower at baseline in the lines without CDCA3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p |
| [[ACBD7]] | C | ACBD7 activity raises NUF2's level | lines that do not express ACBD7 (4) vs lines expressing it (46) | 1.65× lower at baseline in the lines without ACBD7 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000197332, LRP3, PHGDH; maybe low, not absent; its own permutation p |
| [[FAM72D]] | C | FAM72D activity raises NUF2's level | lines that do not express FAM72D (3) vs lines expressing it (47) | 2.20× lower at baseline in the lines without FAM72D | 0.093 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ATP6V1E2, ASAP3, ENSG00000267131; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCP110]] | C | NUF2's natural level weakens CCP110's drug response | NUF2's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.23; direction not clear | 0.069 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.864). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-36.0, -55.5); signed map (-49.0, -41.7). **Vector** length 156, 56.2% of its response variance represented; |z| ≥ 3 in 1,224 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.76 to 12); *G2/M checkpoint* (hallmark, mean cos +0.75 to 9); *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.73 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +4.9 | +5.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | +6.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +0.4 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | +3.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | +4.2 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.6 | +3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.1 | +2.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.1 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.4 | -11.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | -8.4 | -11.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | -7.9 | -8.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | -7.6 | -8.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.6 | -7.2 |
|  | [[EX229 (drug)]] 5 µM |  | -4.7 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.7 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -0.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.6 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | NUF2 component of NDC80 kinetochore complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:163,266,576-163,355,764 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NUF2R, CT106; previously CDCA1 |
| Gene groups (HGNC) | NDC80 kinetochore complex |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZD4](https://www.uniprot.org/uniprotkb/Q9BZD4) (Kinetochore protein Nuf2):

> Acts as a component of the essential kinetochore-associated NDC80 complex, which is required for chromosome segregation and spindle checkpoint activity. Required for kinetochore integrity and the organization of stable microtubule binding sites in the outer plate of the kinetochore. The NDC80 complex synergistically enhances the affinity of the SKA1 complex for microtubules and may allow the NDC80 complex to track depolymerizing microtubules.

**Summary**, from NCBI Gene [83540](https://www.ncbi.nlm.nih.gov/gene/83540):

> This gene encodes a protein that is highly similar to yeast Nuf2, a component of a conserved protein complex associated with the centromere. Yeast Nuf2 disappears from the centromere during meiotic prophase when centromeres lose their connection to the spindle pole body, and plays a regulatory role in chromosome segregation. The encoded protein is found to be associated with centromeres of mitotic HeLa cells, which suggests that this protein is a functional homolog of yeast Nuf2. Alternatively …

**Accessions** — [HGNC:14621](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14621) · Entrez [83540](https://www.ncbi.nlm.nih.gov/gene/83540) · UniProt [Q9BZD4](https://www.uniprot.org/uniprotkb/Q9BZD4) · Ensembl [ENSG00000143228](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143228)

## Data

Gene col 6702: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6702); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6702, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6702]; `tensor/DDL_lfc|DDL_z.npy` [6702]; `embed/gene_vectors.npy` [6702]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6702 or target_col == 6702). Every well: [[NUF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
