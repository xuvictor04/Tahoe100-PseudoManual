---
symbol: "CFAP251"
type: "gene"
col: 8124
ensembl_id: "ENSG00000158023"
name: "cilia and flagella associated protein 251"
location: "12q24.31"
module: 38
arm: "+"
pooled_cpm: 37.52
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# CFAP251

*cilia and flagella associated protein 251* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.84× (z +13.8, q 3e-40, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.643× (z -7.1, q 9e-10, down in 26 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.688× (z -6.0, q 5e-07, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PILRA]] (+0.69, fdr 7e-06), [[CPNE9]] (+0.69, fdr 7e-06), [[C3orf62]] (+0.69, fdr 7e-06); moves opposite to [[FBXO7]] (-0.57, fdr 1e-05), [[CHPT1]] (-0.56, fdr 3e-05), [[KDM1A]] (-0.56, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8124.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.84×** | +13.8 | 3e-40 | 35/47 (J82, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.96×** | +10.8 | 1e-24 | 35/48 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +8.3 | 2e-14 | 28/47 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.61×** | +7.6 | 5e-12 | 27/48 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +4.7 | 2e-04 | 19/48 (A549, RKO, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.6 | 3e-04 | 21/48 (NCI-H2030, A498, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.72×** | +4.6 | 4e-04 | 16/46 (A498, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.32×** | +4.4 | 8e-04 | 22/48 (MIA PaCa-2, KATO III, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.21×** | +4.3 | 0.001 | 19/47 (SHP-77, Hs 766T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.30×** | +4.0 | 0.004 | 15/45 (NCI-H2030, AsPC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.008 | 17/47 (SK-MEL-2, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.073 | 8/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8124.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.643×** | -7.1 | 9e-10 | 26/46 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.688×** | -6.0 | 5e-07 | 26/47 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.672×** | -5.9 | 5e-07 | 23/45 (NCI-H1792, SW480, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.697×** | -5.8 | 1e-06 | 24/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.587×** | -4.5 | 9e-04 | 17/46 (SHP-77, PANC-1, …) | top dose only | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.771×** | -4.2 | 0.003 | 22/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.802×** | -3.5 | 0.033 | 17/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.798×** | -3.4 | 0.045 | 11/47 (SNU-423, SW 1088, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.754×** | -3.2 | 0.068 | 8/44 (HCT15, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.807×** | -3.2 | 0.068 | 11/47 (RKO, A-172, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.682×** | -3.2 | 0.068 | 17/47 (NCI-H1792, H4, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8124. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 413 | 0 | 13 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -16.6) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.188× (z -13.5) |
| [[NCI-H1792 (line)]] | alt | 96.8 | 0 | 13 (7 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0968× (z -19.1) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.252× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 38.7 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.287× (z -10.4) |
| [[PANC-1 (line)]] | alt | 43.3 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -13.3) |
| [[CFPAC-1 (line)]] | alt | 51.8 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.333× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 21.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +8.6) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.124× (z -9.3) |
| [[LoVo (line)]] | wt | 29.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 13.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.167× (z -9.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 57.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.146× (z -17.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +11.0) | — |
| [[HepG2_C3A (line)]] | wt | 21.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 47.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.226× (z -10.0) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.114× (z -11.6) |
| [[J82 (line)]] | alt | 31.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +15.1) | — |
| [[LS 180 (line)]] | wt | 25.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.236× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +10.1) | — |
| [[NCI-H23 (line)]] | alt | 18.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.155× (z -9.6) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 18.3 | 0 | 1 | — | [[NG25 (drug)]] 5 µM 0.0523× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +11.7) | — |
| [[SNU-1 (line)]] | wt | 15.3 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0968× (z -9.7) |
| [[SNU-423 (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8124), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PILRA]] | +0.69 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[CPNE9]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[C3orf62]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.69 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[ROPN1L]] | +0.68 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.68 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.68 | +0.73 / +0.58 | both halves | 8e-06 |  |
| [[IDI2-AS1]] | +0.68 | +0.72 / +0.67 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.67 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[PPIEL]] | +0.67 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.67 | +0.73 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO7]] | -0.57 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[CHPT1]] | -0.56 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[KDM1A]] | -0.56 | -0.63 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.703). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.2, -15.7); signed map (15.9, 9.5). **Vector** length 94.5, 20.3% of its response variance represented; |z| ≥ 3 in 1,222 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +13.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +8.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.9 | +4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.7 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +4.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.2 | -5.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -7.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.0 | -1.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.9 | -3.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.8 | -2.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 251 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:121,918,592-122,003,927 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33630, CaM-IP4; previously WDR66 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TBY9](https://www.uniprot.org/uniprotkb/Q8TBY9) (Cilia- and flagella-associated protein 251):

> Involved in spermatozoa motility. May also regulate cilium motility through its role in the assembly of the axonemal radial spokes (By similarity).

**Summary**, from NCBI Gene [144406](https://www.ncbi.nlm.nih.gov/gene/144406):

> This protein encoded by this gene belongs to the WD repeat-containing family of proteins, which function in the formation of protein-protein complexes in a variety of biological pathways. This family member appears to function in the determination of mean platelet volume (MPV), and polymorphisms in this gene have been associated with variance in MPV. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:28506](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28506) · Entrez [144406](https://www.ncbi.nlm.nih.gov/gene/144406) · UniProt [Q8TBY9](https://www.uniprot.org/uniprotkb/Q8TBY9) · Ensembl [ENSG00000158023](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158023)

## Data

Gene col 8124: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8124); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8124, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8124]; `tensor/DDL_lfc|DDL_z.npy` [8124]; `embed/gene_vectors.npy` [8124]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8124 or target_col == 8124). Every well: [[CFAP251 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP251.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
