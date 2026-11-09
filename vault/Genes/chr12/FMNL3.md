---
symbol: "FMNL3"
type: "gene"
col: 8452
ensembl_id: "ENSG00000161791"
name: "formin like 3"
location: "12q13.12"
module: 13
arm: "+"
pooled_cpm: 33.01
n_lines_expressing: 42
n_dd_up: 19
n_dd_down: 8
n_dd_up_clean: 15
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 21
direction_downstream: 8
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# FMNL3

*formin like 3* — 12q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.78× (z +33.0, q 0e+00, up in 39 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.620× (z -8.4, q 3e-14, down in 24 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R18]] (+0.60, fdr 2e-05), [[SPHK1]] (+0.60, fdr 6e-05), [[RFTN1]] (+0.59, fdr 2e-05); moves opposite to [[GUSBP1]] (-0.52, fdr 1e-04), [[ATRN]] (-0.51, fdr 4e-05), [[GLG1]] (-0.49, fdr 1e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[LINC00702]] → it (grade B ⚠); 8 go from it, the strongest it → [[NBPF26]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8452.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.78×** | +33.0 | 0e+00 | 39/39 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.26×** | +28.0 | 0e+00 | 39/40 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +10.4 | 3e-23 | 25/40 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +9.5 | 4e-19 | 20/38 (NCI-H2347, NCI-H23, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +8.7 | 3e-16 | 25/39 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.58×** | +8.0 | 1e-13 | 27/40 (SW1417, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +7.6 | 2e-12 | 20/40 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +6.8 | 7e-10 | 20/40 (PANC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.35×** | +5.2 | 1e-05 | 19/40 (SW480, C32, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +5.0 | 4e-05 | 20/40 (NCI-H1792, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.34×** | +4.8 | 9e-05 | 14/31 (A-427, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.7 | 1e-04 | 16/38 (PANC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +4.4 | 5e-04 | 18/40 (A-427, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +4.2 | 0.001 | 10/28 (HEC-1-A, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.001 | 18/40 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.9 | 0.003 | 18/40 (C-33 A, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.005 | 15/40 (PANC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.028 | 11/40 (LoVo, RKO, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.073 | 9/40 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8452.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.620×** | -8.4 | 3e-14 | 24/40 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.720×** | -5.8 | 2e-06 | 18/40 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.596×** | -4.7 | 4e-04 | 19/39 (hTERT-HPNE, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.782×** | -4.3 | 0.002 | 15/39 (Hs 766T, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.806×** | -4.2 | 0.003 | 14/40 (HOP62, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.810×** | -3.7 | 0.019 | 12/40 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.811×** | -3.7 | 0.019 | 13/40 (HOP62, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.814×** | -3.6 | 0.021 | 16/40 (A-172, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.868× | -3.4 | 0.046 | 11/40 (HOP62, PANC-1, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.845× | -3.3 | 0.055 | 13/40 (HOP62, SW 1088, …) | all doses, flat | noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.837× | -3.1 | 0.089 | 12/40 (NCI-H460, SW 900, …) | top dose only |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.841× | -3.0 | 0.11 | 11/40 (SW 1088, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8452. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 89.4 | 4 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +20.9) | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -11.1) |
| [[PANC-1 (line)]] | alt | 49.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.32× (z +29.2) | — |
| [[HS-578T (line)]] | alt | 83.7 | 4 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 8.02× (z +15.4) | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -8.9) |
| [[C32 (line)]] | wt | 29.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +13.7) | — |
| [[NCI-H1792 (line)]] | alt | 38.7 | 3 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 9.20× (z +16.6) | [[Bortezomib (drug)]] 5 µM 0.0976× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 21.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.89× (z +24.0) | — |
| [[NCI-H460 (line)]] | wt | 15.7 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 7.80× (z +15.4) | — |
| [[A498 (line)]] | wt | 23.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +15.1) | — |
| [[HEC-1-A (line)]] | alt | 21.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +12.8) | — |
| [[NCI-H23 (line)]] | alt | 34.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +11.8) | — |
| [[RKO (line)]] | wt | 64.4 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.41× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -12.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 20.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.44× (z +14.7) | — |
| [[BT-474 (line)]] | alt | 8.90 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.2× (z +17.0) | — |
| [[HepG2_C3A (line)]] | wt | 8.98 | 0 | 2 | — | [[Sunitinib (drug)]] 0.05 µM 0.0789× (z -9.1) |
| [[HOP62 (line)]] | alt | 70.6 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.91× (z +11.1) | [[Adagrasib (drug)]] 0.05 µM 0.579× (z -12.8) ⚠ position not correctable |
| [[Hs 766T (line)]] | wt | 41.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.6) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.284× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 139 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 6.85× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.265× (z -8.5) |
| [[J82 (line)]] | alt | 48.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +16.8) | — |
| [[NCI-H2030 (line)]] | alt | 15.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.93× (z +18.1) | — |
| [[Panc 03.27 (line)]] | alt | 16.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.3× (z +20.2) | — |
| [[SK-MEL-2 (line)]] | alt | 63.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +15.2) | — |
| [[SNU-423 (line)]] | alt | 54.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.42× (z +19.2) | — |
| [[SW1417 (line)]] | alt | 16.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +17.7) | — |
| [[A-427 (line)]] | wt | 39.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 25.1 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.159× (z -9.4) |
| [[CHP-212 (line)]] | wt | 24.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +11.3) | — |
| [[H4 (line)]] | wt | 76.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 5.08× (z +10.0) | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0874× (z -9.1) |
| [[LoVo (line)]] | wt | 19.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 16.5 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 6.09× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 92.4 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 6.68× (z +15.3) | — |
| [[SNU-1 (line)]] | wt | 15.0 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.124× (z -8.5) ⚠ toxic |
| [[SW480 (line)]] | alt | 34.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.7) | — |
| [[A549 (line)]] | wt | 8.13 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 92.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.11 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.49 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8452), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R18]] | +0.60 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[SPHK1]] | +0.60 | +0.70 / +0.38 | both halves | 6e-05 |  |
| [[RFTN1]] | +0.59 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[EVA1A]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ARHGAP31]] | +0.58 | +0.52 / +0.52 | both halves | 1e-05 | pathway: CDC42 GTPase cycle; STRING 456 |
| [[ATP2C2-AS1]] | +0.58 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[PHLDB1]] | +0.57 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[COL7A1]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SEPTIN8]] | +0.56 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[TRAF1]] | +0.55 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[MMRN2]] | +0.55 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[LINC00973]] | +0.55 | +0.56 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUSBP1]] | -0.52 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[ATRN]] | -0.51 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[GLG1]] | -0.49 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[TYW1]] | -0.48 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[MRPL55]] | -0.47 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[ZFP14]] | -0.47 | -0.44 / -0.37 | both halves | 7e-05 |  |
| [[FBXO21]] | -0.47 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[RNF41]] | -0.47 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[CAPN7]] | -0.47 | -0.37 / -0.44 | both halves | 9e-05 |  |
| [[NCK1]] | -0.47 | -0.42 / -0.36 | both halves | 9e-05 | pathway: RHO GTPase Effectors |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 21, C 0. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00702]] | B | LINC00702 activity raises FMNL3's level | lines that do not express LINC00702 (25) vs lines expressing it (25) | 3.74× lower at baseline in the lines without LINC00702 | 8e-04 | ⚠ within organs, on part of the lines; also absent: FGF5, ENSG00000253553, LNCOG |
| [[FGF5]] | B | FGF5 activity raises FMNL3's level | lines that do not express FGF5 (28) vs lines expressing it (22) | 3.26× lower at baseline in the lines without FGF5 | 0.003 | ⚠ within organs, on part of the lines; also absent: INSYN2B, CFAP299, LINC00702 |
| [[AFF3]] | B | AFF3 activity raises FMNL3's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 3.19× lower at baseline in the lines without AFF3 | 0.008 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[RFTN1]] | B | RFTN1 activity raises FMNL3's level | lines that do not express RFTN1 (20) vs lines expressing it (30) | 3.18× lower at baseline in the lines without RFTN1 | 0.013 | ⚠ within organs, on part of the lines; also absent: GPR176, KIAA0408, COL12A1 |
| [[SOCS2]] | B | SOCS2 activity raises FMNL3's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 3.27× lower at baseline in the lines without SOCS2 | 0.020 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A |
| [[CDH13]] | B | CDH13 activity raises FMNL3's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.95× lower at baseline in the lines without CDH13 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[AKT3]] | B | AKT3 activity raises FMNL3's level | lines that do not express AKT3 (16) vs lines expressing it (34) | 3.09× lower at baseline in the lines without AKT3 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000234405, GNB4, LINC03041 |
| [[RPSAP52]] | B | RPSAP52 activity raises FMNL3's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 2.51× lower at baseline in the lines without RPSAP52 | 0.042 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[APCDD1L-DT]] | B | APCDD1L-DT activity raises FMNL3's level | lines that do not express APCDD1L-DT (26) vs lines expressing it (24) | 2.37× lower at baseline in the lines without APCDD1L-DT | 0.049 | ⚠ within organs, on part of the lines; also absent: TENM4, ITGA11, APCDD1L; maybe low, not absent |
| [[COL5A3]] | B | COL5A3 activity raises FMNL3's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 2.24× lower at baseline in the lines without COL5A3 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[ROBO4]] | B | ROBO4 activity raises FMNL3's level | lines that do not express ROBO4 (28) vs lines expressing it (22) | 2.76× lower at baseline in the lines without ROBO4 | 0.060 | ⚠ within organs, on part of the lines; also absent: LNCOG, ENSG00000222032, PHACTR1 |
| [[SOCS2-AS1]] | B | SOCS2-AS1 activity raises FMNL3's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 2.64× lower at baseline in the lines without SOCS2-AS1 | 0.061 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NBPF26]] | B | FMNL3 activity raises NBPF26's level | lines that do not express FMNL3 (8) vs lines expressing it (42) | 2.41× lower at baseline in the lines without FMNL3 | 0.012 | ⚠ within organs, on part of the lines; also absent: STARD9, CERCAM, ASAP3 |
| [[CAPN7]] | B | FMNL3 activity raises CAPN7's level | lines that do not express FMNL3 (8) vs lines expressing it (42) | 1.42× lower at baseline in the lines without FMNL3 | 0.016 | ⚠ within organs, on part of the lines; also absent: STARD9, CERCAM, ASAP3 |
| [[PHF19]] | B | FMNL3 activity raises PHF19's level | lines that do not express FMNL3 (8) vs lines expressing it (42) | 1.69× lower at baseline in the lines without FMNL3 | 0.052 | ⚠ within organs, on part of the lines; also absent: STARD9, CERCAM, ASAP3 |
| [[SYNGAP1]] | B | FMNL3 activity raises SYNGAP1's level | lines that do not express FMNL3 (8) vs lines expressing it (42) | 1.55× lower at baseline in the lines without FMNL3 | 0.058 | ⚠ within organs, on part of the lines; also absent: STARD9, CERCAM, ASAP3 |
| [[LHFPL6]] | B | FMNL3 activity raises LHFPL6's level | lines that do not express FMNL3 (8) vs lines expressing it (42) | 4.01× lower at baseline in the lines without FMNL3 | 0.059 | ⚠ within organs, on part of the lines; also absent: STARD9, CERCAM, ASAP3 |
| [[SEPTIN11]] | B | FMNL3 activity raises SEPTIN11's level | lines that do not express FMNL3 (8) vs lines expressing it (42) | 1.56× lower at baseline in the lines without FMNL3 | 0.091 | ⚠ within organs, on part of the lines; also absent: STARD9, CERCAM, ASAP3 |
| [[TMEFF1]] | B | FMNL3 activity raises TMEFF1's level | lines that do not express FMNL3 (8) vs lines expressing it (42) | 2.63× lower at baseline in the lines without FMNL3 | 0.095 | ⚠ within organs, on part of the lines; also absent: STARD9, CERCAM, ASAP3 |
| [[CYREN]] | B | FMNL3 activity raises CYREN's level | lines that do not express FMNL3 (8) vs lines expressing it (42) | 1.28× lower at baseline in the lines without FMNL3 | 0.098 | ⚠ within organs, on part of the lines; also absent: STARD9, CERCAM, ASAP3 |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.408). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.3, -2.6); signed map (18.8, 43.8). **Vector** length 114, 29.0% of its response variance represented; |z| ≥ 3 in 1,070 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.4 | +28.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.4 | +33.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +4.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change | +5.7 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +0.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.5 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +3.0 |
| fall | [[NG25 (drug)]] 5 µM |  | -5.0 | -4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | -8.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -2.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -5.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.0 | -2.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.0 | -1.8 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.0 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | formin like 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.12 — chr12:49,636,499-49,708,165 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp762B245, MGC45819, WBP3 |
| Gene groups (HGNC) | Armadillo like helical domain containing; Formins |
| Reactome | 9 pathways, smallest: RHOJ GTPase cycle; RHOC GTPase cycle; RHO GTPases Activate Formins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVF7](https://www.uniprot.org/uniprotkb/Q8IVF7) (Formin-like protein 3):

> Plays a role in the regulation of cell morphology and cytoskeletal organization. Required in the control of cell shape and migration. Required for developmental angiogenesis (By similarity). In this process, required for microtubule reorganization and for efficient endothelial cell elongation. In quiescent endothelial cells, triggers rearrangement of the actin cytoskeleton, but does not alter microtubule alignment.

**Summary**, from NCBI Gene [91010](https://www.ncbi.nlm.nih.gov/gene/91010):

> The protein encoded by this gene contains a formin homology 2 domain and has high sequence identity to the mouse Wbp3 protein. Two alternative transcripts encoding different isoforms have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:23698](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23698) · Entrez [91010](https://www.ncbi.nlm.nih.gov/gene/91010) · UniProt [Q8IVF7](https://www.uniprot.org/uniprotkb/Q8IVF7) · Ensembl [ENSG00000161791](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161791)

## Data

Gene col 8452: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8452); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8452, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8452]; `tensor/DDL_lfc|DDL_z.npy` [8452]; `embed/gene_vectors.npy` [8452]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8452 or target_col == 8452). Every well: [[FMNL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FMNL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
