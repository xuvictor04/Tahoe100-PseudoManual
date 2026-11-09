---
symbol: "COL27A1"
type: "gene"
col: 12276
ensembl_id: "ENSG00000196739"
name: "collagen type XXVII alpha 1 chain"
location: "9q32"
module: 80
arm: "+"
pooled_cpm: 68.83
n_lines_expressing: 38
n_dd_up: 8
n_dd_down: 26
n_dd_up_clean: 6
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 4
direction_downstream: 13
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# COL27A1

*collagen type XXVII alpha 1 chain* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.56× (z +25.8, q 0e+00, up in 31 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.270× (z -25.4, q 0e+00, down in 35 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IPO9-AS1]] (+0.61, fdr 1e-05), [[ARHGAP31]] (+0.60, fdr 1e-05), [[C2orf92]] (+0.60, fdr 3e-05); moves opposite to [[MRPS31P5-1]] (-0.58, fdr 3e-05), [[UBXN2B]] (-0.56, fdr 2e-04), [[PRUNE1]] (-0.56, fdr 3e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 13 go from it, the strongest it → [[GNG12-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12276.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.56×** | +25.8 | 0e+00 | 31/36 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +8.2 | 5e-14 | 24/36 (A498, Hs 766T, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.47×** | +7.1 | 2e-10 | 22/35 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.7 | 3e-04 | 17/36 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.5 | 9e-04 | 14/34 (Hs 766T, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 0.003 | 14/36 (LOX-IMVI, RPMI-7951, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.23×** | +4.1 | 0.004 | 12/36 (A498, A-172, …) | rises with dose |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.012 | 12/36 (J82, SNU-423, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.19× | +3.4 | 0.044 | 6/36 (LoVo, HEC-1-A, …) | inconsistent across doses |  |
| [[Ritonavir (drug)]] 5 µM |  | 1.13× | +3.4 | 0.044 | 6/36 (MIA PaCa-2, KATO III, …) | rises with dose |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.082 | 9/36 (RPMI-7951, SNU-423, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12276.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.270×** | -25.4 | 0e+00 | 35/36 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.277×** | -24.9 | 0e+00 | 34/36 (SNU-423, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.334×** | -21.2 | 0e+00 | 34/36 (RKO, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.504×** | -13.3 | 4e-38 | 29/36 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.524×** | -12.0 | 3e-31 | 28/34 (RKO, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.542×** | -11.8 | 2e-30 | 26/35 (SNU-423, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.544×** | -11.8 | 4e-30 | 30/36 (NCI-H1792, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.546×** | -11.7 | 8e-30 | 27/36 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.626×** | -9.1 | 8e-18 | 27/36 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.637×** | -8.7 | 2e-16 | 23/36 (NCI-H1792, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.632×** | -8.5 | 7e-16 | 28/35 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.657×** | -7.8 | 3e-13 | 22/36 (RKO, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.476×** | -7.5 | 2e-12 | 28/36 (RKO, SNU-423, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.684×** | -7.3 | 9e-12 | 26/36 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.686×** | -7.3 | 1e-11 | 21/36 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -7.0 | 6e-11 | 22/37 (RKO, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.500×** | -7.0 | 8e-11 | 25/36 (MIA PaCa-2, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.712×** | -6.6 | 2e-09 | 21/36 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.590×** | -5.3 | 2e-06 | 24/35 (KATO III, RKO, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12276. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 78.2 | 1 | 14 (7 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +13.8) | [[Homoharringtonine (drug)]] 5 µM 0.0990× (z -29.1) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.143× (z -17.3) |
| [[RKO (line)]] | wt | 289 | 1 | 13 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +17.5) | [[Panobinostat (drug)]] 0.5 µM 0.139× (z -25.8) |
| [[J82 (line)]] | alt | 189 | 0 | 13 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.296× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.199× (z -16.4) |
| [[KATO III (line)]] | alt | 84.0 | 1 | 12 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -18.8) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.191× (z -16.7) |
| [[NCI-H1792 (line)]] | alt | 151 | 0 | 13 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -19.8) |
| [[SNU-423 (line)]] | alt | 144 | 0 | 12 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.114× (z -22.9) |
| [[A498 (line)]] | wt | 192 | 3 (1 ⚠) | 4 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.214× (z -17.8) |
| [[C-33 A (line)]] | alt | 42.8 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 185 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.136× (z -13.7) |
| [[LoVo (line)]] | wt | 37.0 | 3 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.47× (z +20.5) | [[Belinostat (drug)]] 5 µM 0.230× (z -14.2) |
| [[A-172 (line)]] | wt | 172 | 1 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.68× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.171× (z -23.5) |
| [[H4 (line)]] | wt | 154 | 2 | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +12.0) | [[Belinostat (drug)]] 5 µM 0.257× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 68.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -19.6) ⚠ cell-cycle shift, explains ~75% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.256× (z -12.5) |
| [[SW48 (line)]] | wt | 78.8 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +11.9) | [[Belinostat (drug)]] 5 µM 0.201× (z -11.6) |
| [[A549 (line)]] | wt | 74.6 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +18.3) | [[Panobinostat (drug)]] 5 µM 0.314× (z -11.7) |
| [[CFPAC-1 (line)]] | alt | 35.7 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.192× (z -12.5) |
| [[HepG2_C3A (line)]] | wt | 192 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +10.4) ⚠ cell-cycle shift, explains ~75% of this change | [[Panobinostat (drug)]] 5 µM 0.207× (z -13.9) |
| [[HOP62 (line)]] | alt | 110 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +16.5) | [[Panobinostat (drug)]] 5 µM 0.208× (z -18.0) |
| [[Hs 766T (line)]] | wt | 131 | 2 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +22.2) | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -16.1) |
| [[Panc 03.27 (line)]] | alt | 32.9 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +14.9) | [[Belinostat (drug)]] 5 µM 0.230× (z -11.4) |
| [[PANC-1 (line)]] | alt | 31.8 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 157 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -16.2) |
| [[HT-29 (line)]] | alt | 42.2 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +12.3) | [[Digitoxin (drug)]] 5 µM 0.339× (z -9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.352× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 150 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +10.6) | [[Belinostat (drug)]] 5 µM 0.204× (z -15.4) |
| [[NCI-H460 (line)]] | wt | 22.2 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.07× (z +23.9) | — |
| [[HS-578T (line)]] | alt | 60.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.264× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 34.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +13.4) | — |
| [[SK-MEL-2 (line)]] | alt | 28.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change |
| [[AN3 CA (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.4) ⚠ cell-cycle shift, explains ~75% of this change |
| [[NCI-H2030 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -9.1) ⚠ cell-cycle shift, explains ~75% of this change |
| [[SNU-1 (line)]] | wt | 30.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 22.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +11.4) | — |
| [[A-427 (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.04 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.13 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 70.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.02 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.80 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.92 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 7.04 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 77.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.2 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 12.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12276), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO9-AS1]] | +0.61 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ARHGAP31]] | +0.60 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[C2orf92]] | +0.60 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[ZNF341-AS1]] | +0.59 | +0.50 / +0.38 | both halves | 6e-05 |  |
| [[WNT5B]] | +0.58 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CCDC26]] | +0.57 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[STARD4-AS1]] | +0.57 | +0.38 / +0.48 | both halves | 7e-05 |  |
| [[CDK6-AS1]] | +0.57 | +0.38 / +0.47 | both halves | 6e-05 |  |
| [[PTPRG]] | +0.57 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[ACTR3-AS1]] | +0.57 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[LINC01358]] | +0.56 | +0.44 / +0.39 | both halves | 6e-05 |  |
| [[GCNT4]] | +0.56 | +0.45 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPS31P5-1]] | -0.58 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[UBXN2B]] | -0.56 | -0.29 / -0.65 | both halves | 2e-04 |  |
| [[PRUNE1]] | -0.56 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[STX7]] | -0.55 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[CNEP1R1]] | -0.54 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[BTBD3]] | -0.54 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[MRPS31P4]] | -0.54 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[TMEM245]] | -0.53 | -0.37 / -0.45 | both halves | 8e-05 | same gene group |
| [[ALAD]] | -0.53 | -0.20 / -0.53 | both halves | 7e-04 |  |
| [[GUSBP18]] | -0.52 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[COMMD2]] | -0.52 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[ARNT]] | -0.52 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers COL27A1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC03041]] | B | LINC03041 activity raises COL27A1's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 2.58× lower at baseline in the lines without LINC03041 | 0.014 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[WNT5B]] | B | WNT5B activity raises COL27A1's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 2.22× lower at baseline in the lines without WNT5B | 0.054 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1 |
| [[TOP2B]] | B | TOP2B activity lowers COL27A1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNG12-AS1]] | B | COL27A1 activity raises GNG12-AS1's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 1.54× lower at baseline in the lines without COL27A1 | 0.023 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[C9orf24]] | B | COL27A1 activity raises C9orf24's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 2.36× lower at baseline in the lines without COL27A1 | 0.029 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[ARHGAP31]] | B | COL27A1 activity raises ARHGAP31's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 3.30× lower at baseline in the lines without COL27A1 | 0.032 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[NEK10]] | B | COL27A1 activity raises NEK10's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 2.35× lower at baseline in the lines without COL27A1 | 0.035 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[SERPINB6]] | B | COL27A1 activity raises SERPINB6's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 1.88× lower at baseline in the lines without COL27A1 | 0.044 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[FLI1]] | B | COL27A1 activity raises FLI1's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 3.94× lower at baseline in the lines without COL27A1 | 0.049 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[CAVIN4]] | B | COL27A1 activity raises CAVIN4's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 2.07× lower at baseline in the lines without COL27A1 | 0.051 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[PTPRG]] | B | COL27A1 activity raises PTPRG's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 2.61× lower at baseline in the lines without COL27A1 | 0.058 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[IMMP1L]] | B | COL27A1 activity lowers IMMP1L's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 1.35× higher at baseline in the lines without COL27A1 | 0.062 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| [[ACTR3-AS1]] | B | COL27A1 activity raises ACTR3-AS1's level | lines that do not express COL27A1 (12) vs lines expressing it (38) | 1.79× lower at baseline in the lines without COL27A1 | 0.075 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM | B | COL27A1 activity lowers the cells' numbers under Bisoprolol (hemifumarate) 0.5 µM (makes them more sensitive) | lines that do not express COL27A1 (12) vs lines expressing it (36) | the lines without COL27A1: 1.27× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |
| cells under [[Amsacrine (drug)]] 5 µM | B | COL27A1 activity lowers the cells' numbers under Amsacrine 5 µM (makes them more sensitive) | lines that do not express COL27A1 (12) vs lines expressing it (36) | the lines without COL27A1: 1.16× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: C13orf46, ENSG00000285804, GSDME; maybe low, not absent |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.6, -5.9); signed map (25.6, 9.4). **Vector** length 113, 31.6% of its response variance represented; |z| ≥ 3 in 1,241 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +13.7 | +25.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.8 | +7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.9 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | -2.9 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +1.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.6 | -24.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.4 | -7.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.1 | -11.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.1 | -21.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.8 | -4.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.7 | -7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -5.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XXVII alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:114,155,537-114,312,511 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1870, MGC11337, FLJ11895 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Fibrillar collagens |
| Reactome | 14 pathways, smallest: Developmental Lineage of Pancreatic Ductal Cells; Developmental Lineage of Pancreatic Endocrine Mid Progenitor Cells; Developmental Cell Lineages of the Endocrine Pancreas |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IZC6](https://www.uniprot.org/uniprotkb/Q8IZC6) (Collagen alpha-1(XXVII) chain):

> Plays a role during the calcification of cartilage and the transition of cartilage to bone.

**Summary**, from NCBI Gene [85301](https://www.ncbi.nlm.nih.gov/gene/85301):

> This gene encodes a member of the fibrillar collagen family, and plays a role during the calcification of cartilage and the transition of cartilage to bone. The encoded protein product is a preproprotein. It includes an N-terminal signal peptide, which is followed by an N-terminal propetide, mature peptide and a C-terminal propeptide. The N-terminal propeptide contains thrombospondin N-terminal-like and laminin G-like domains. The mature peptide is a major triple-helical region. The C-terminal …

**Accessions** — [HGNC:22986](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22986) · Entrez [85301](https://www.ncbi.nlm.nih.gov/gene/85301) · UniProt [Q8IZC6](https://www.uniprot.org/uniprotkb/Q8IZC6) · Ensembl [ENSG00000196739](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196739)

## Data

Gene col 12276: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12276); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12276, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12276]; `tensor/DDL_lfc|DDL_z.npy` [12276]; `embed/gene_vectors.npy` [12276]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12276 or target_col == 12276). Every well: [[COL27A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL27A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
