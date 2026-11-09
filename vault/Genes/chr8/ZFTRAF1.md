---
symbol: "ZFTRAF1"
type: "gene"
col: 11960
ensembl_id: "ENSG00000187954"
name: "zinc finger TRAF-type and ring finger containing 1"
location: "8q24.3"
module: 138
arm: "+"
pooled_cpm: 5.65
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# ZFTRAF1

*zinc finger TRAF-type and ring finger containing 1* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.01× (z +10.8, q 3e-24, up in 35 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.536× (z -6.9, q 2e-09, down in 26 of 45 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Abemaciclib (drug)]] 0.5 µM: 0.586× (z -4.3, q 0.006, down in 11 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TEPSIN]] (+0.79, fdr 7e-06), [[GSK3A]] (+0.66, fdr 1e-05), [[WDR45]] (+0.63, fdr 1e-05); moves opposite to [[FIGNL1]] (-0.56, fdr 2e-05), [[PDSS1]] (-0.54, fdr 3e-05), [[ADH5]] (-0.54, fdr 3e-05).
> It is in [[Module 138]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11960.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +10.8 | 3e-24 | 35/41 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +5.9 | 1e-06 | 3/12 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.57×** | +5.1 | 7e-05 | 11/26 (SW1417, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.8 | 2e-04 | 16/37 (C32, A-427, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +4.7 | 3e-04 | 9/35 (Panc 03.27, HS-578T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +4.6 | 3e-04 | 14/38 (HEC-1-A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.49×** | +4.4 | 7e-04 | 9/47 (Hs 766T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.3 | 0.001 | 14/45 (HEC-1-A, HOP62, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 0.001 | 13/45 (H4, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.002 | 14/46 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.003 | 13/45 (MIA PaCa-2, BT-474, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.9 | 0.004 | 11/32 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.049 | 2/31 (Panc 03.27, PANC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.049 | 7/43 (HT-29, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.077 | 7/43 (SHP-77, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.079 | 5/41 (SW480, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.22×** | +3.0 | 0.079 | 8/38 (COLO 205, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11960.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.536×** | -6.9 | 2e-09 | 26/45 (NCI-H2030, AsPC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.586×** | -4.3 | 0.006 | 11/46 (AsPC-1, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.491×** | -4.1 | 0.006 | 15/38 (A-427, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.686×** | -4.0 | 0.009 | 14/44 (Hs 766T, SHP-77, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.507×** | -4.0 | 0.009 | 14/37 (A-427, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.520×** | -3.8 | 0.013 | 9/42 (A-427, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.526×** | -3.7 | 0.015 | 12/40 (KATO III, HT-29, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.791×** | -3.5 | 0.027 | 15/45 (A498, SW48, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.547×** | -3.5 | 0.027 | 9/43 (hTERT-HPNE, Hs 766T, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11960. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 7.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 7.78 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.107× (z -8.7) |
| [[C32 (line)]] | wt | 5.16 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0671× (z -8.7) |
| [[HS-578T (line)]] | alt | 6.43 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0891× (z -9.8) |
| [[HT-29 (line)]] | alt | 8.40 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 6.50 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.138× (z -9.2) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 6.21 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0894× (z -8.8) ⚠ toxic; unreliable plate only |
| [[SW1417 (line)]] | alt | 8.73 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.74 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11960), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TEPSIN]] | +0.79 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[GSK3A]] | +0.66 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[WDR45]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[FBRS]] | +0.62 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[DNMT3A]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[UBXN6]] | +0.60 | +0.42 / +0.69 | both halves | 4e-05 |  |
| [[CLCN7]] | +0.60 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[SETD1B]] | +0.60 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[CYTH2]] | +0.60 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[ZNF740]] | +0.60 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[DMWD]] | +0.59 | +0.67 / +0.40 | both halves | 5e-05 |  |
| [[KMT2B]] | +0.59 | +0.73 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FIGNL1]] | -0.56 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[PDSS1]] | -0.54 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[ADH5]] | -0.54 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[BOLA3]] | -0.53 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[DLAT]] | -0.53 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[CCT8]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PPAT]] | -0.52 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[HLTF]] | -0.52 | -0.51 / -0.44 | both halves | 3e-05 | same gene group |
| [[GGCT]] | -0.52 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[RADX]] | -0.52 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[WDR36]] | -0.51 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[POT1]] | -0.51 | -0.55 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.746). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.1, -22.0); signed map (3.2, -7.3). **Vector** length 62.7, 9.42% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +10.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.9 | +4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +2.8 | +4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +2.7 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +5.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.0 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -3.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.0 | -4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[EX229 (drug)]] 5 µM |  | -2.9 | -4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.8 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger TRAF-type and ring finger containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,449,582-144,462,871 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CHRP, KIAA0496, MGC13010; previously CYHR1 |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers TRAF-type; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

UniProt [P0DTL6](https://www.uniprot.org/uniprotkb/P0DTL6) carries no function annotation.

**Summary**, from NCBI Gene [50626](https://www.ncbi.nlm.nih.gov/gene/50626):

> Predicted to enable zinc ion binding activity. Predicted to be located in nuclear envelope and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17806](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17806) · Entrez [50626](https://www.ncbi.nlm.nih.gov/gene/50626) · UniProt [P0DTL6](https://www.uniprot.org/uniprotkb/P0DTL6) · Ensembl [ENSG00000187954](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187954)

## Data

Gene col 11960: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11960); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11960, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11960]; `tensor/DDL_lfc|DDL_z.npy` [11960]; `embed/gene_vectors.npy` [11960]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11960 or target_col == 11960). Every well: [[ZFTRAF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFTRAF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
