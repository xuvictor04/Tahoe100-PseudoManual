---
symbol: "MTRF1"
type: "gene"
col: 4198
ensembl_id: "ENSG00000120662"
name: "mitochondrial translation release factor 1"
location: "13q14.11"
module: 23
arm: "+"
pooled_cpm: 17.59
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# MTRF1

*mitochondrial translation release factor 1* — 13q14.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.58× (z +9.1, q 7e-17, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.537× (z -12.3, q 5e-32, down in 35 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.454× (z -8.2, q 3e-14, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF234]] (+0.66, fdr 1e-05), [[TAS2R4]] (+0.66, fdr 1e-05), [[YARS2]] (+0.66, fdr 1e-05); moves opposite to [[ZMIZ2]] (-0.57, fdr 3e-05), [[ECE1]] (-0.56, fdr 3e-05), [[EML4]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4198.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +9.1 | 7e-17 | 32/47 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.35×** | +8.3 | 3e-14 | 27/48 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.6 | 1e-08 | 24/46 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.34×** | +5.8 | 9e-07 | 17/48 (LOX-IMVI, KATO III, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +5.0 | 5e-05 | 16/48 (LS 180, Hs 766T, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +4.9 | 8e-05 | 17/47 (A498, C-33 A, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.19× | +4.8 | 1e-04 | 14/48 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.26×** | +4.4 | 9e-04 | 15/48 (LS 180, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~10% of this change | **1.24×** | +4.1 | 0.002 | 16/44 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.22×** | +3.9 | 0.006 | 9/47 (A549, NCI-H2030, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.013 | 5/47 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.6 | 0.013 | 10/48 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~72% of this change | 1.19× | +3.5 | 0.024 | 6/48 (HT-29, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.028 | 5/47 (CFPAC-1, PANC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.031 | 10/47 (A498, SW480, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.3 | 0.039 | 3/48 (LoVo, A498, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.12× | +3.2 | 0.041 | 6/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.17× | +3.2 | 0.042 | 7/48 (LS 180, Hs 766T, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.16× | +3.0 | 0.079 | 4/47 (KATO III, HT-29, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | 1.16× | +2.9 | 0.089 | 6/47 (C32, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4198.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.537×** | -12.3 | 5e-32 | 35/46 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.609×** | -9.8 | 3e-20 | 28/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.629×** | -9.2 | 8e-18 | 30/47 (BT-474, SW480, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.649×** | -8.2 | 3e-14 | 26/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.454×** | -8.2 | 3e-14 | 27/48 (KATO III, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.671×** | -7.9 | 2e-13 | 25/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.676×** | -7.5 | 7e-12 | 22/47 (NCI-H1792, RKO, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.722×** | -6.4 | 8e-09 | 19/47 (COLO 205, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.540×** | -6.4 | 1e-08 | 24/45 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.774×** | -5.1 | 2e-05 | 17/48 (COLO 205, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.836× | -5.0 | 3e-05 | 21/47 (SNU-423, LoVo, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.783×** | -4.9 | 6e-05 | 13/48 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.847× | -3.1 | 0.067 | 6/47 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.853× | -3.1 | 0.067 | 12/48 (RPMI-7951, HOP62, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 0.896× | -3.1 | 0.085 | 4/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.748×** | -3.0 | 0.095 | 9/46 (Hs 766T, H4, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4198. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 34.8 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.308× (z -13.6) ⚠ cell-cycle shift, explains ~35% of this change |
| [[COLO 205 (line)]] | alt | 83.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 36.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 17.8 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.378× (z -9.6) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SW48 (line)]] | wt | 16.1 | 0 | 2 | — | [[Bendamustine (drug)]] 5 µM 0.119× (z -8.8) |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0955× (z -10.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[H4 (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0671× (z -9.9) ⚠ cell-cycle shift, explains ~92% of this change |
| [[HT-29 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0595× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.251× (z -8.9) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H23 (line)]] | alt | 17.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.243× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change |
| [[Panc 03.27 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.207× (z -10.4) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.154× (z -9.4) ⚠ cell-cycle shift, explains ~73% of this change |
| [[SNU-423 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4198), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF234]] | +0.66 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[TAS2R4]] | +0.66 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[YARS2]] | +0.66 | +0.54 / +0.49 | both halves | 1e-05 | STRING 571 |
| [[PAAF1]] | +0.64 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[ARMCX5-GPRASP2]] | +0.63 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[LINC01134]] | +0.62 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[PGLS-DT]] | +0.61 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[ZNF529-AS1]] | +0.61 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[NOXRED1]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ZFHX2-AS1]] | +0.60 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[CCDC59]] | +0.60 | +0.61 / +0.40 | both halves | 4e-05 |  |
| [[UQCC1]] | +0.60 | +0.42 / +0.52 | both halves | 4e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMIZ2]] | -0.57 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[ECE1]] | -0.56 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[EML4]] | -0.54 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[H2AZ2]] | -0.54 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[PADI2]] | -0.54 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[MED14]] | -0.53 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[UNC13B]] | -0.53 | -0.44 / -0.37 | both halves | 9e-05 |  |
| [[LSM4]] | -0.52 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[RHPN1]] | -0.52 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[BTBD3]] | -0.51 | -0.48 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.567). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (-1.8, 18.2); signed map (22.6, -12.7). **Vector** length 73.8, 12.7% of its response variance represented; |z| ≥ 3 in 968 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.8 | +9.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | +4.6 | +8.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~10% of this change | +3.7 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +2.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | +2.9 | +5.8 |
|  | [[EX229 (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +4.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.4 | +5.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +0.8 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.2 | -5.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.1 | -6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -0.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.5 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -0.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.4 | -1.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial translation release factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.11 — chr13:41,216,369-41,263,577 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RF1, MTTRF1, MGC47721 |
| Gene groups (HGNC) | Mitochondrial translation release factor family |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 3 pathways, smallest: Mitochondrial translation termination; Mitochondrial translation; Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [O75570](https://www.uniprot.org/uniprotkb/O75570) (Peptide chain release factor 1, mitochondrial):

> Mitochondrial peptide chain release factor that directs the termination of translation in response to the peptide chain non-canonical stop codons AGG and AGA. Non-canonical termination codons AGG and AGA are found at the end of MT-CO1/COX1 and MT-ND6/ND6 open reading frames, respectively. Recognizes non-canonical stop codons via a network of interactions between the codon, MTRF1 and the ribosomal RNA (rRNA): in contrast to other translation release factors, which identify the codon in the …

**Summary**, from NCBI Gene [9617](https://www.ncbi.nlm.nih.gov/gene/9617):

> The protein encoded by this gene was determined by in silico methods to be a mitochondrial protein with similarity to the peptide chain release factors (RFs) discovered in bacteria and yeast. The peptide chain release factors direct the termination of translation in response to the peptide chain termination codons. Initially thought to have a role in the termination of mitochondria protein synthesis, a recent publication found no mitochondrial translation release functionality. Multiple …

**Accessions** — [HGNC:7469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7469) · Entrez [9617](https://www.ncbi.nlm.nih.gov/gene/9617) · UniProt [O75570](https://www.uniprot.org/uniprotkb/O75570) · Ensembl [ENSG00000120662](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120662)

## Data

Gene col 4198: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4198); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4198, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4198]; `tensor/DDL_lfc|DDL_z.npy` [4198]; `embed/gene_vectors.npy` [4198]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4198 or target_col == 4198). Every well: [[MTRF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTRF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
