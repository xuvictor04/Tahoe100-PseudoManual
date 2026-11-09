---
symbol: "CBY1"
type: "gene"
col: 1891
ensembl_id: "ENSG00000100211"
name: "chibby 1, beta catenin antagonist"
location: "22q13.1"
module: 12
arm: "+"
pooled_cpm: 14.69
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# CBY1

*chibby 1, beta catenin antagonist* — 22q13.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.414× (z -12.9, q 2e-35, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFV3]] (+0.70, fdr 7e-06), [[AARSD1]] (+0.62, fdr 1e-05), [[ACAD10]] (+0.62, fdr 1e-05); moves opposite to [[GNAL]] (-0.55, fdr 6e-05), [[DDX3X]] (-0.55, fdr 8e-05), [[PPIA]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1891.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.28× | +3.6 | 0.17 | 12/47 (SNU-423, CFPAC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.26× | +3.4 | 0.20 | 10/48 (SW480, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~12% of this change | 1.26× | +3.3 | 0.20 | 15/42 (AsPC-1, NCI-H1573, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1891.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.414×** | -12.9 | 2e-35 | 38/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.438×** | -12.1 | 4e-31 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.439×** | -12.1 | 4e-31 | 35/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.302×** | -9.2 | 7e-18 | 42/48 (NCI-H1573, Hs 766T, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.319×** | -8.7 | 3e-16 | 37/44 (Hs 766T, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.568×** | -8.3 | 1e-14 | 32/47 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.602×** | -7.1 | 8e-11 | 24/45 (HCT15, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.736×** | -6.3 | 2e-08 | 23/47 (HOP62, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.662×** | -6.0 | 1e-07 | 31/47 (LoVo, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.688×** | -5.5 | 3e-06 | 24/48 (J82, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.767×** | -5.4 | 3e-06 | 20/48 (Hs 766T, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.505×** | -5.2 | 8e-06 | 22/36 (NCI-H1573, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.702×** | -5.2 | 1e-05 | 21/47 (C32, BT-474, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.784×** | -5.0 | 2e-05 | 19/45 (Hs 766T, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.716×** | -4.6 | 2e-04 | 17/47 (SW48, HEC-1-A, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.608×** | -3.8 | 0.005 | 16/45 (COLO 205, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.813×** | -3.0 | 0.074 | 6/48 (NCI-H2030, BT-474, …) | rises with dose |  |
| [[Auranofin (drug)]] 0.5 µM |  | **0.818×** | -2.9 | 0.096 | 8/48 (NCI-H661, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1891. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 18.4 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -12.7) |
| [[NCI-H1792 (line)]] | alt | 17.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -10.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 20.0 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.151× (z -10.7) |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -12.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.271× (z -9.3) |
| [[Hs 766T (line)]] | wt | 19.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -9.9) |
| [[HS-578T (line)]] | alt | 20.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -9.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[hTERT-HPNE (line)]] | wt | 9.73 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -12.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0689× (z -9.8) |
| [[J82 (line)]] | alt | 11.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.4) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.189× (z -9.7) |
| [[PANC-1 (line)]] | alt | 13.3 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -12.1) |
| [[SK-MEL-2 (line)]] | alt | 24.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -10.2) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -9.6) |
| [[SW48 (line)]] | wt | 14.3 | 0 | 2 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0857× (z -9.1) |
| [[BT-474 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.211× (z -8.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0926× (z -9.7) ⚠ toxic |
| [[H4 (line)]] | wt | 15.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -8.5) ⚠ cell-cycle shift, explains ~37% of this change |
| [[MIA PaCa-2 (line)]] | alt | 25.6 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.112× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.0746× (z -9.1) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 7.22 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -11.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[Panc 03.27 (line)]] | alt | 13.4 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0401× (z -9.1) |
| [[SHP-77 (line)]] | alt | 24.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -8.9) |
| [[SNU-423 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -9.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[A-172 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1891), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFV3]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[AARSD1]] | +0.62 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[ACAD10]] | +0.62 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[TAB1]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[VCPKMT]] | +0.60 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[FRA10AC1]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[AP3S2]] | +0.59 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[COQ4]] | +0.59 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ZSWIM9]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[RBMX2]] | +0.59 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[MTRES1]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[DENND6B]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAL]] | -0.55 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[DDX3X]] | -0.55 | -0.37 / -0.59 | both halves | 8e-05 |  |
| [[PPIA]] | -0.53 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[NXT2]] | -0.53 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[NQO1]] | -0.52 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[MAPRE1]] | -0.51 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[YWHAZ]] | -0.51 | -0.46 / -0.58 | both halves | 3e-05 | pathway: Deactivation of the beta-catenin transactivating complex; STRING 992 |
| [[SUMO3]] | -0.51 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[YWHAQ]] | -0.50 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.50 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[AXDND1]] | -0.50 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[CCN3]] | -0.49 | -0.32 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.513). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-35.5, -8.6); signed map (-16.3, -12.9). **Vector** length 60.3, 9.43% of its response variance represented; |z| ≥ 3 in 929 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~12% of this change | +3.0 | +3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +2.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.3 | -1.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.1 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -5.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.4 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | chibby 1, beta catenin antagonist |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:38,656,636-38,673,854 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PIGEA14, PIGEA-14, Chibby, Cby, Chibby1; previously C22orf2, PGEA1 |
| Reactome | 3 pathways, smallest: Deactivation of the beta-catenin transactivating complex; TCF dependent signaling in response to WNT; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3M2](https://www.uniprot.org/uniprotkb/Q9Y3M2) (Protein chibby homolog 1):

> Inhibits the Wnt/Wingless pathway by binding to CTNNB1/beta-catenin and inhibiting beta-catenin-mediated transcriptional activation through competition with TCF/LEF transcription factors. Has also been shown to play a role in regulating the intracellular trafficking of polycystin-2/PKD2 and possibly of other intracellular proteins. Promotes adipocyte and cardiomyocyte differentiation (By similarity).

**Summary**, from NCBI Gene [25776](https://www.ncbi.nlm.nih.gov/gene/25776):

> Beta-catenin is a transcriptional activator and oncoprotein involved in the development of several cancers. The protein encoded by this gene interacts directly with the C-terminal region of beta-catenin, inhibiting oncogenic beta-catenin-mediated transcriptional activation by competing with transcription factors for binding to beta-catenin. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1307) · Entrez [25776](https://www.ncbi.nlm.nih.gov/gene/25776) · UniProt [Q9Y3M2](https://www.uniprot.org/uniprotkb/Q9Y3M2) · Ensembl [ENSG00000100211](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100211)

## Data

Gene col 1891: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1891); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1891, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1891]; `tensor/DDL_lfc|DDL_z.npy` [1891]; `embed/gene_vectors.npy` [1891]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1891 or target_col == 1891). Every well: [[CBY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
