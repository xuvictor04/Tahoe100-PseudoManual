---
symbol: "TAF6"
type: "gene"
col: 2740
ensembl_id: "ENSG00000106290"
name: "TATA-box binding protein associated factor 6"
location: "7q22.1"
module: 127
arm: "+"
pooled_cpm: 18.02
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# TAF6

*TATA-box binding protein associated factor 6* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.98× (z +19.9, q 0e+00, up in 39 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.97× (z +12.4, q 8e-33, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.729× (z -5.8, q 4e-06, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRPF8]] (+0.75, fdr 7e-06), [[GTF3C1]] (+0.72, fdr 7e-06), [[DCTN1]] (+0.72, fdr 7e-06); moves opposite to [[MSX1]] (-0.62, fdr 1e-04), [[ZCCHC10]] (-0.60, fdr 5e-05), [[SPATC1]] (-0.58, fdr 7e-05).
> It is in [[Module 127]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2740.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.98×** | +19.9 | 0e+00 | 39/42 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +18.3 | 0e+00 | 25/27 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.97×** | +12.4 | 8e-33 | 45/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +11.7 | 2e-29 | 44/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +11.0 | 6e-26 | 42/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +10.8 | 3e-25 | 30/36 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +4.8 | 1e-04 | 0/48 | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.3 | 0.002 | 16/48 (LOX-IMVI, Hs 766T, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.007 | 10/48 (NCI-H1573, J82, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **1.22×** | +3.5 | 0.026 | 11/45 (A-427, NCI-H1573, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.21×** | +3.4 | 0.030 | 8/48 (LoVo, A498, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.035 | 10/48 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.41×** | +3.3 | 0.046 | 6/48 (KATO III, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.052 | 7/46 (SW480, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2740.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.729×** | -5.8 | 4e-06 | 25/48 (C32, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.744×** | -5.4 | 2e-05 | 22/46 (AsPC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.799×** | -4.0 | 0.014 | 17/47 (AN3 CA, SHP-77, …) | rises with dose |  |
| [[Sulfisoxazole (drug)]] 5 µM |  | 0.864× | -3.8 | 0.022 | 7/48 (PANC-1, LS 180, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.820×** | -3.6 | 0.032 | 17/47 (C32, SW 1271, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.689×** | -3.6 | 0.036 | 10/47 (NCI-H661, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.830×** | -3.4 | 0.045 | 11/48 (AsPC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.830×** | -3.4 | 0.045 | 9/48 (SNU-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | **0.832×** | -3.4 | 0.046 | 3/48 (HEC-1-A, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.885× | -3.2 | 0.084 | 7/48 (NCI-H1573, NCI-H1792, …) | rises with dose |  |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | 0.839× | -3.1 | 0.100 | 9/47 (AN3 CA, NCI-H2030, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2740. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 34.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 21.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +14.4) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 17.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +10.6) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 15.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.62× (z +10.7) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 19.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.06× (z +10.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 30.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +11.6) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 15.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.53× (z +13.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 25.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.87× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 23.8 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.399× (z -9.9) |
| [[A549 (line)]] | wt | 15.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +8.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 26.3 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.108× (z -8.5) |
| [[C-33 A (line)]] | alt | 26.0 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.147× (z -11.2) |
| [[C32 (line)]] | wt | 26.1 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.202× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 5 µM 0.0587× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 16.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +8.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +10.2) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.223× (z -8.5) ⚠ cell-cycle shift, explains ~42% of this change |
| [[AsPC-1 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2740), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPF8]] | +0.75 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[GTF3C1]] | +0.72 | +0.58 / +0.72 | both halves | 7e-06 |  |
| [[DCTN1]] | +0.72 | +0.70 / +0.71 | both halves | 7e-06 | pathway: Affinity selection of immunoglobulins |
| [[SNRNP200]] | +0.70 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[COPS6]] | +0.69 | +0.62 / +0.71 | both halves | 7e-06 | ⚠ same locus (14.7 kb: neighbours can correlate without regulation) |
| [[AP2M1]] | +0.69 | +0.66 / +0.60 | both halves | 7e-06 | pathway: HIV Infection |
| [[TGOLN2]] | +0.67 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[EIF4H]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[EMC1]] | +0.66 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[BLTP2]] | +0.64 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[GPS1]] | +0.64 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[CDK16]] | +0.64 | +0.52 / +0.70 | both halves | 1e-05 |  |
| [[UGGT1]] | +0.64 | +0.57 / +0.60 | both halves | 9e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSX1]] | -0.62 | -0.33 / -0.65 | both halves | 1e-04 |  |
| [[ZCCHC10]] | -0.60 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[SPATC1]] | -0.58 | -0.38 / -0.61 | both halves | 7e-05 |  |
| [[RPL36AL]] ⚠ | -0.57 | -0.53 / -0.66 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NACA4P]] ⚠ | -0.56 | -0.47 / -0.62 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF503]] | -0.56 | -0.37 / -0.57 | both halves | 8e-05 |  |
| [[ZBTB7A]] | -0.56 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[EAF1-AS1]] | -0.55 | -0.42 / -0.56 | both halves | 4e-05 |  |
| [[UBE2CP5]] | -0.55 | -0.38 / -0.59 | both halves | 7e-05 |  |
| [[LINC00685]] | -0.55 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[SNHG8]] | -0.55 | -0.37 / -0.58 | both halves | 8e-05 |  |
| [[CTBP1-AS]] ⚠ | -0.55 | -0.45 / -0.52 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[A2ML1-AS1]] | -0.55 | -0.48 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.748). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-27.7, -22.9); signed map (-21.0, -36.8). **Vector** length 77.7, 13.8% of its response variance represented; |z| ≥ 3 in 848 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +18.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +19.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +10.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.2 | +3.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +11.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +1.3 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +1.3 | +1.4 |
|  | [[Pentoxifylline (drug)]] 0.5 µM |  | +1.3 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.6 | -5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.6 | -5.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.4 | -2.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | TATA-box binding protein associated factor 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,106,876-100,119,841 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TAFII70, TAFII80, MGC:8964, TAFII85; previously TAF2E |
| Gene groups (HGNC) | Armadillo like helical domain containing; General transcription factor IID complex subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 20 pathways, smallest: HIV Transcription Initiation; RNA Polymerase II HIV Promoter Escape; RNA Polymerase II Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [P49848](https://www.uniprot.org/uniprotkb/P49848) (Transcription initiation factor TFIID subunit 6):

> The TFIID basal transcription factor complex plays a major role in the initiation of RNA polymerase II (Pol II)-dependent transcription. TFIID recognizes and binds promoters with or without a TATA box via its subunit TBP, a TATA-box-binding protein, and promotes assembly of the pre-initiation complex (PIC). The TFIID complex consists of TBP and TBP-associated factors (TAFs), including TAF1, TAF2, TAF3, TAF4, TAF5, TAF6, TAF7, TAF8, TAF9, TAF10, TAF11, TAF12 and TAF13. The TFIID complex …

**Summary**, from NCBI Gene [6878](https://www.ncbi.nlm.nih.gov/gene/6878):

> Initiation of transcription by RNA polymerase II requires the activities of more than 70 polypeptides. The protein that coordinates these activities is transcription factor IID (TFIID), which binds to the core promoter to position the polymerase properly, serves as the scaffold for assembly of the remainder of the transcription complex, and acts as a channel for regulatory signals. TFIID is composed of the TATA-binding protein (TBP) and a group of evolutionarily conserved proteins known as …

**Accessions** — [HGNC:11540](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11540) · Entrez [6878](https://www.ncbi.nlm.nih.gov/gene/6878) · UniProt [P49848](https://www.uniprot.org/uniprotkb/P49848) · Ensembl [ENSG00000106290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106290)

## Data

Gene col 2740: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2740); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2740, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2740]; `tensor/DDL_lfc|DDL_z.npy` [2740]; `embed/gene_vectors.npy` [2740]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2740 or target_col == 2740). Every well: [[TAF6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAF6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
