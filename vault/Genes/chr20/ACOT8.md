---
symbol: "ACOT8"
type: "gene"
col: 2146
ensembl_id: "ENSG00000101473"
name: "acyl-CoA thioesterase 8"
location: "20q13.12"
module: 183
arm: "+"
pooled_cpm: 12.62
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# ACOT8

*acyl-CoA thioesterase 8* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.66× (z +7.9, q 1e-12, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.469× (z -11.7, q 5e-29, down in 43 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.657× (z -6.5, q 1e-08, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRIM23]] (+0.77, fdr 7e-06), [[C1orf50]] (+0.74, fdr 7e-06), [[UBA3]] (+0.73, fdr 7e-06); moves opposite to [[MAPRE1]] (-0.67, fdr 7e-06), [[NCR3LG1]] (-0.61, fdr 4e-05), [[EIF4G1]] (-0.61, fdr 1e-05).
> It is in [[Module 183]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2146.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.66×** | +7.9 | 1e-12 | 30/47 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +7.9 | 1e-12 | 35/48 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +7.4 | 4e-11 | 21/45 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.58×** | +7.0 | 3e-10 | 30/48 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.49×** | +6.1 | 1e-07 | 26/47 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +4.8 | 1e-04 | 17/43 (A-172, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.003 | 9/47 (KATO III, AsPC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.003 | 10/46 (J82, RKO, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +4.0 | 0.003 | 5/47 (AsPC-1, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +4.0 | 0.004 | 13/38 (LOX-IMVI, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.27×** | +3.7 | 0.013 | 15/42 (NCI-H2347, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.013 | 8/43 (KATO III, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.020 | 12/48 (AsPC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.037 | 6/48 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.046 | 6/45 (NCI-H2347, SW 900, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2146.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.469×** | -11.7 | 5e-29 | 43/47 (NCI-H460, NCI-H2030, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.608×** | -7.4 | 3e-11 | 23/39 (Hs 766T, HS-578T, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.657×** | -6.5 | 1e-08 | 24/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.691×** | -5.7 | 1e-06 | 22/47 (NCI-H460, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.758×** | -4.3 | 0.002 | 17/46 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.600×** | -4.1 | 0.003 | 13/45 (Hs 766T, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.609×** | -4.0 | 0.005 | 12/43 (Hs 766T, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.615×** | -3.9 | 0.006 | 11/44 (COLO 205, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.636×** | -3.7 | 0.016 | 13/42 (RPMI-7951, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.638×** | -3.6 | 0.016 | 10/44 (SNU-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Volasertib (drug)]] 0.5 µM |  | **0.723×** | -3.6 | 0.017 | 6/48 (RKO, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.799×** | -3.5 | 0.023 | 7/47 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.819×** | -3.1 | 0.085 | 5/47 (KATO III, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2146. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.1 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0964× (z -16.1) |
| [[AsPC-1 (line)]] | alt | 9.07 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -9.2) ⚠ cell-cycle shift, explains ~13% of this change |
| [[HT-29 (line)]] | alt | 17.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 8.71 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -9.6) ⚠ cell-cycle shift, explains ~13% of this change |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.285× (z -8.7) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2146), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM23]] | +0.77 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[C1orf50]] | +0.74 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[UBA3]] | +0.73 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[TTI2]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[ZER1]] | +0.67 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[CRBN]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ASB8]] | +0.67 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[CWC15]] | +0.66 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[USP30]] | +0.66 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[ZNHIT3]] | +0.66 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[CIR1]] | +0.65 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[MTIF3]] | +0.65 | +0.58 / +0.66 | both halves | 8e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPRE1]] | -0.67 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[NCR3LG1]] | -0.61 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[EIF4G1]] | -0.61 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[THOC6]] | -0.60 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | -0.59 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[SFPQ]] | -0.57 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[HNRNPA2B1]] | -0.56 | -0.46 / -0.52 | both halves | 2e-05 |  |
| [[HNRNPAB]] | -0.55 | -0.51 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction 0.726). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.7, -5.6); signed map (-21.8, -8.8). **Vector** length 69.1, 11.9% of its response variance represented; |z| ≥ 3 in 730 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +2.9 | +2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +6.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +4.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.7 | +7.9 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +1.6 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +4.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.3 | -7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.1 | -0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.0 | +1.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -3.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA thioesterase 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,841,721-45,857,405 (-) |
| Ensembl biotype | protein_coding |
| Also known as | hACTE-III, hTE, PTE-2, NAP1; previously PTE1 |
| Gene groups (HGNC) | Acyl-CoA thioesterases; Thioester hydrolases |
| Hallmark sets | PEROXISOME, FATTY_ACID_METABOLISM |
| Reactome | 13 pathways, smallest: Beta-oxidation of pristanoyl-CoA; Beta-oxidation of very long chain fatty acids; alpha-linolenic (omega3) and linoleic (omega6) acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O14734](https://www.uniprot.org/uniprotkb/O14734) (Acyl-coenzyme A thioesterase 8):

> Catalyzes the hydrolysis of acyl-CoAs into free fatty acids and coenzyme A (CoASH), regulating their respective intracellular levels. Displays no strong substrate specificity with respect to the carboxylic acid moiety of Acyl-CoAs (By similarity). Hydrolyzes medium length (C2 to C20) straight-chain, saturated and unsaturated acyl-CoAS but is inactive towards substrates with longer aliphatic chains. Moreover, it catalyzes the hydrolysis of CoA esters of bile acids, such as choloyl-CoA and …

**Summary**, from NCBI Gene [10005](https://www.ncbi.nlm.nih.gov/gene/10005):

> The protein encoded by this gene is a peroxisomal thioesterase that appears to be involved more in the oxidation of fatty acids rather than in their formation. The encoded protein can bind to the human immunodeficiency virus-1 protein Nef, and mediate Nef-induced down-regulation of CD4 in T-cells. [provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:15919](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15919) · Entrez [10005](https://www.ncbi.nlm.nih.gov/gene/10005) · UniProt [O14734](https://www.uniprot.org/uniprotkb/O14734) · Ensembl [ENSG00000101473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101473)

## Data

Gene col 2146: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2146); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2146, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2146]; `tensor/DDL_lfc|DDL_z.npy` [2146]; `embed/gene_vectors.npy` [2146]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2146 or target_col == 2146). Every well: [[ACOT8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACOT8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
