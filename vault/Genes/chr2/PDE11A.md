---
symbol: "PDE11A"
type: "gene"
col: 4910
ensembl_id: "ENSG00000128655"
name: "phosphodiesterase 11A"
location: "2q31.2"
module: 27
arm: "+"
pooled_cpm: 8.46
n_lines_expressing: 46
n_dd_up: 22
n_dd_down: 18
n_dd_up_clean: 14
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 7
direction_downstream: 2
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# PDE11A

*phosphodiesterase 11A* — 2q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.92× (z +18.6, q 0e+00, up in 35 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.475× (z -9.1, q 6e-17, down in 25 of 43 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RGS6]] (+0.63, fdr 7e-06), [[NCALD]] (+0.62, fdr 8e-06), [[NPSR1-AS1]] (+0.53, fdr 3e-05); moves opposite to [[VCPKMT]] (-0.42, fdr 7e-04), [[MAU2]] (-0.42, fdr 4e-04), [[UNKL]] (-0.41, fdr 9e-05).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[DSCAML1]] → it (grade B ⚠); 2 go from it, the strongest it → [[CASC8]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4910.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.92×** | +18.6 | 0e+00 | 35/42 (LS 180, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +11.9 | 2e-30 | 25/36 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.52×** | +11.3 | 2e-27 | 29/39 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.08×** | +8.5 | 2e-15 | 24/43 (LS 180, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.96×** | +8.1 | 6e-14 | 20/41 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.87×** | +7.7 | 1e-12 | 13/25 (LoVo, NCI-H460, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.79×** | +7.2 | 6e-11 | 23/40 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.77×** | +7.0 | 2e-10 | 22/43 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.78×** | +6.5 | 4e-09 | 5/16 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.64×** | +6.1 | 6e-08 | 16/42 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.5 | 2e-06 | 13/42 (SW480, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.50×** | +4.8 | 7e-05 | 3/13 (PANC-1, HOP62, …) | all doses, flat | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.44×** | +4.3 | 7e-04 | 9/36 (SW480, NCI-H2030, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.92×** | +4.2 | 0.001 | 9/40 (CFPAC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.41×** | +4.0 | 0.002 | 11/39 (A549, CFPAC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.062 | 7/39 (SW480, LOX-IMVI, …) | inconsistent across doses |  |
| [[Afatinib (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.062 | 6/42 (AsPC-1, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.088 | 2/39 (HOP62, KATO III) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.27×** | +2.9 | 0.089 | 4/41 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Brimonidine (drug)]] 5 µM |  | **1.27×** | +2.9 | 0.089 | 1/43 (A498) | rises with dose |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.28×** | +2.9 | 0.089 | 4/42 (SW480, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4910.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.475×** | -9.1 | 6e-17 | 25/43 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.530×** | -7.7 | 3e-12 | 21/42 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.529×** | -7.6 | 4e-12 | 22/41 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.537×** | -7.6 | 4e-12 | 24/36 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.552×** | -7.1 | 1e-10 | 21/39 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.646×** | -5.0 | 5e-05 | 14/38 (A-172, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.664×** | -4.9 | 8e-05 | 17/40 (KATO III, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.785×** | -4.2 | 0.002 | 15/42 (HepG2/C3A, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.711×** | -3.9 | 0.005 | 14/43 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.729×** | -3.8 | 0.006 | 11/43 (HepG2/C3A, CFPAC-1, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.730×** | -3.8 | 0.006 | 11/35 (LOX-IMVI, AsPC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.728×** | -3.7 | 0.009 | 14/30 (KATO III, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vilanterol (drug)]] 5 µM |  | **0.819×** | -3.4 | 0.026 | 10/41 (KATO III, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.760×** | -3.2 | 0.053 | 16/41 (HepG2/C3A, A549, …) | top dose only | composition shift |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.770×** | -3.2 | 0.057 | 11/42 (hTERT-HPNE, SW 900, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.773×** | -3.1 | 0.063 | 8/42 (SW1417, NCI-H2030, …) | inconsistent across doses |  |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.781×** | -3.0 | 0.089 | 5/43 (LOX-IMVI, NCI-H1573, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.629×** | -3.0 | 0.098 | 9/37 (HEC-1-A, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4910. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 35.8 | 1 | 7 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.93× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0874× (z -11.6) |
| [[SW480 (line)]] | alt | 11.7 | 2 | 6 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.10× (z +12.0) | [[Digitoxin (drug)]] 5 µM 0.143× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -11.4) |
| [[KATO III (line)]] | alt | 11.0 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.04× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0797× (z -10.5) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.114× (z -9.2) |
| [[LoVo (line)]] | wt | 6.16 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 3.62× (z +8.6) | [[Digitoxin (drug)]] 0.5 µM 0.135× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 11.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.106× (z -9.8) |
| [[LS 180 (line)]] | wt | 8.26 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 9.27× (z +14.2) | — |
| [[NCI-H23 (line)]] | alt | 5.98 | 0 | 2 (1 ⚠) | — | [[Hesperidin (drug)]] 5 µM 0.0784× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 2.88 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.73× (z +10.6) | — |
| [[A-172 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A498 (line)]] | wt | 48.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 12.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.65× (z +11.0) | — |
| [[COLO 205 (line)]] | alt | 8.28 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0612× (z -9.1) ⚠ toxic |
| [[HT-29 (line)]] | alt | 3.12 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.87× (z +9.0) | — |
| [[PANC-1 (line)]] | alt | 2.33 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.84× (z +8.5) | — |
| [[SK-MEL-2 (line)]] | alt | 9.69 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW1417 (line)]] | alt | 8.45 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.43× (z +8.6) | — |
| [[A-427 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4910), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RGS6]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[NCALD]] | +0.62 | +0.58 / +0.61 | both halves | 8e-06 | **novel candidate** |
| [[NPSR1-AS1]] | +0.53 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[SUSD4]] | +0.52 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[CPNE4]] | +0.52 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[DNAH6]] | +0.52 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ENTREP2]] | +0.51 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[MTUS2]] | +0.50 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[LINC01811]] | +0.50 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[MROH7]] | +0.50 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[SLAIN1]] | +0.49 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[CYP2J2]] | +0.49 | +0.43 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VCPKMT]] | -0.42 | -0.20 / -0.45 | both halves | 7e-04 |  |
| [[MAU2]] | -0.42 | -0.26 / -0.50 | both halves | 4e-04 |  |
| [[UNKL]] | -0.41 | -0.36 / -0.50 | both halves | 9e-05 |  |
| [[VPS33A]] | -0.41 | -0.15 / -0.56 | ⚠ one half (not replicated) | 0.001 |  |
| [[ZNF595]] | -0.41 | -0.37 / -0.31 | both halves | 2e-04 |  |
| [[SLC25A16]] | -0.41 | -0.26 / -0.40 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSCAML1]] | B | DSCAML1 activity raises PDE11A's level | lines that do not express DSCAML1 (37) vs lines expressing it (13) | 2.42× lower at baseline in the lines without DSCAML1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FXYD2, ITIH2, FGG |
| [[RAPGEF5]] | B | RAPGEF5 activity raises PDE11A's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 1.96× lower at baseline in the lines without RAPGEF5 | 0.031 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[KRT23]] | B | KRT23 activity raises PDE11A's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 1.89× lower at baseline in the lines without KRT23 | 0.033 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP |
| [[RAPGEF5]] | B | RAPGEF5 activity strengthens PDE11A's drug response | lines that do not express RAPGEF5 (14) vs lines expressing it (29) | the lines without RAPGEF5 respond 0.75× as strongly (z diff +0.46); strongest at Digitoxin 0.5 µM: 0.71x vs 0.39x (z diff +2.9) | 0.068 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[LINC00992]] | B | LINC00992 activity raises PDE11A's level | lines that do not express LINC00992 (28) vs lines expressing it (22) | 1.68× lower at baseline in the lines without LINC00992 | 0.074 | ⚠ within organs, on part of the lines; also absent: LINC02147, INPP5D, LGR5 |
| [[LINC01814]] | B | LINC01814 activity raises PDE11A's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 1.54× lower at baseline in the lines without LINC01814 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3 |
| [[NCALD]] | B | NCALD activity raises PDE11A's level | lines that do not express NCALD (18) vs lines expressing it (32) | 1.66× lower at baseline in the lines without NCALD | 0.098 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASC8]] | C | PDE11A activity lowers CASC8's level | lines that do not express PDE11A (4) vs lines expressing it (46) | 3.94× higher at baseline in the lines without PDE11A | 0.033 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: XIRP2, ENSG00000214803, ENSG00000228566; maybe low, not absent |
| [[LINC02694]] | C | PDE11A activity raises LINC02694's level | lines that do not express PDE11A (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without PDE11A | 0.068 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: XIRP2, ENSG00000214803, ENSG00000228566; maybe low, not absent |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.458). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.1, 40.7); signed map (55.5, 15.8). **Vector** length 69.1, 11.5% of its response variance represented; |z| ≥ 3 in 1,138 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +18.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.6 | +11.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | +6.6 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +6.4 | +7.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +11.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +5.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.2 | +2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -3.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -7.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -0.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | phosphodiesterase 11A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q31.2 — chr2:177,623,244-178,108,339 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Phosphodiesterases |
| Reactome | 7 pathways, smallest: cGMP effects; Nitric oxide stimulates guanylate cyclase; Platelet homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCR9](https://www.uniprot.org/uniprotkb/Q9HCR9) (Dual 3',5'-cyclic-AMP and -GMP phosphodiesterase 11A):

> Plays a role in signal transduction by regulating the intracellular concentration of cyclic nucleotides cAMP and cGMP. Catalyzes the hydrolysis of both cAMP and cGMP to 5'-AMP and 5'-GMP, respectively.

**Summary**, from NCBI Gene [50940](https://www.ncbi.nlm.nih.gov/gene/50940):

> The 3',5'-cyclic nucleotides cAMP and cGMP function as second messengers in a wide variety of signal transduction pathways. 3',5'-cyclic nucleotide phosphodiesterases (PDEs) catalyze the hydrolysis of cAMP and cGMP to the corresponding 5'-monophosphates and provide a mechanism to downregulate cAMP and cGMP signaling. This gene encodes a member of the PDE protein superfamily. Mutations in this gene are a cause of Cushing disease and adrenocortical hyperplasia. Multiple transcript variants …

**Accessions** — [HGNC:8773](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8773) · Entrez [50940](https://www.ncbi.nlm.nih.gov/gene/50940) · UniProt [Q9HCR9](https://www.uniprot.org/uniprotkb/Q9HCR9) · Ensembl [ENSG00000128655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128655)

## Data

Gene col 4910: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4910); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4910, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4910]; `tensor/DDL_lfc|DDL_z.npy` [4910]; `embed/gene_vectors.npy` [4910]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4910 or target_col == 4910). Every well: [[PDE11A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDE11A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
