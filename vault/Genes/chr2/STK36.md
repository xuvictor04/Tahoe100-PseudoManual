---
symbol: "STK36"
type: "gene"
col: 8699
ensembl_id: "ENSG00000163482"
name: "serine/threonine kinase 36"
location: "2q35"
module: 127
arm: "+"
pooled_cpm: 8.18
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# STK36

*serine/threonine kinase 36* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.70× (z +8.3, q 6e-14, up in 32 of 47 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.32× (z +4.3, q 0.002, up in 16 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.523× (z -7.2, q 3e-10, down in 29 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.621× (z -5.3, q 2e-05, down in 21 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP13A1]] (+0.72, fdr 8e-06), [[BAP1]] (+0.66, fdr 7e-06), [[U2AF2]] (+0.64, fdr 1e-05); moves opposite to [[ARFGAP3]] (-0.54, fdr 4e-05), [[SLC25A5]] (-0.53, fdr 5e-05), [[PPFIA1]] (-0.53, fdr 6e-05).
> It is in [[Module 127]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8699.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.70×** | +8.3 | 6e-14 | 32/47 (NCI-H1573, RKO, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.58×** | +4.6 | 1e-03 | 12/24 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.49×** | +4.4 | 0.002 | 18/44 (HCT15, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.3 | 0.002 | 16/46 (HEC-1-A, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +3.9 | 0.012 | 6/18 (PANC-1, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.017 | 14/45 (RKO, NCI-H1573, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.035 | 8/46 (CFPAC-1, LS 180, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.32× | +3.1 | 0.15 | 8/46 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8699.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.523×** | -7.2 | 3e-10 | 29/43 (LS 180, HCT15, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.599×** | -5.7 | 3e-06 | 27/46 (LS 180, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.591×** | -5.6 | 4e-06 | 18/38 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.621×** | -5.3 | 2e-05 | 21/45 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.728×** | -5.0 | 6e-05 | 22/46 (SW480, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.641×** | -4.9 | 7e-05 | 17/45 (LS 180, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.652×** | -4.8 | 2e-04 | 20/46 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.794×** | -3.6 | 0.019 | 12/47 (MIA PaCa-2, H4, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.725×** | -3.6 | 0.021 | 15/45 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.736×** | -3.4 | 0.037 | 17/47 (NCI-H460, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **0.748×** | -3.2 | 0.057 | 10/44 (Panc 03.27, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.748×** | -3.2 | 0.057 | 17/45 (SW48, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8699. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 6.82 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0605× (z -11.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[RKO (line)]] | wt | 8.91 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0835× (z -9.6) |
| [[A-427 (line)]] | wt | 6.76 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0638× (z -11.4) |
| [[A549 (line)]] | wt | 6.07 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0868× (z -8.6) |
| [[AN3 CA (line)]] | alt | 13.3 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.05 µM 0.0360× (z -9.3) |
| [[COLO 205 (line)]] | alt | 9.97 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0985× (z -8.7) |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0919× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 7.27 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.189× (z -8.6) ⚠ toxic |
| [[HOP62 (line)]] | alt | 5.70 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0771× (z -11.4) |
| [[Hs 766T (line)]] | wt | 4.44 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM 0.0704× (z -9.0) |
| [[LoVo (line)]] | wt | 5.00 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0734× (z -10.8) |
| [[NCI-H1573 (line)]] | alt | 8.02 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.163× (z -8.9) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.158× (z -10.0) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 7.25 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.107× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 15.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0396× (z -14.9) |
| [[SK-MEL-2 (line)]] | alt | 8.72 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0690× (z -11.3) |
| [[SNU-423 (line)]] | alt | 9.36 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8699), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP13A1]] | +0.72 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[BAP1]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[U2AF2]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[PRPF31]] | +0.64 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[STK11IP]] | +0.63 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[VPS52]] | +0.63 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[DMAP1]] | +0.62 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[MTX1]] | +0.62 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[DHX38]] | +0.60 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[INTS3]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[EMC1]] | +0.59 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[DCTN1]] | +0.59 | +0.41 / +0.63 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARFGAP3]] | -0.54 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[SLC25A5]] | -0.53 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[PPFIA1]] | -0.53 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[PLIN3]] | -0.53 | -0.36 / -0.52 | both halves | 9e-05 |  |
| [[RPS15]] ⚠ | -0.52 | -0.39 / -0.52 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ARID3A]] | -0.52 | -0.23 / -0.59 | both halves | 5e-04 |  |
| [[PPP1R13B]] | -0.51 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[RPS13]] ⚠ | -0.51 | -0.37 / -0.52 | both halves | 8e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[KATNBL1]] | -0.50 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[RPL36AL]] ⚠ | -0.50 | -0.37 / -0.46 | both halves | 9e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL18]] ⚠ | -0.50 | -0.31 / -0.50 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-32.5, -3.8); signed map (-12.1, -30.6). **Vector** length 66.5, 10.2% of its response variance represented; |z| ≥ 3 in 941 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.6 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.0 | +1.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +3.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | -5.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.2 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -5.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.4 | -0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.0 | -4.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.9 | -3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | serine/threonine kinase 36 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:218,672,069-218,702,716 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1278, FU |
| Gene groups (HGNC) | Armadillo like helical domain containing; Unc-51 like kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRP7](https://www.uniprot.org/uniprotkb/Q9NRP7) (Serine/threonine-protein kinase 36):

> Serine/threonine protein kinase which plays an important role in the smoothened pathway by regulating the activity of GLI transcription factors. Controls the activity of the transcriptional regulators GLI1, GLI2 and GLI3 by opposing the effect of SUFU and promoting their nuclear localization. Acts by mediating phosphorylation of GLI proteins, promoting their dissociation from SUFU. Also catalyzes phosphorylation of ULK4 adapter. GLI2 requires an additional function of STK36 to become …

**Summary**, from NCBI Gene [27148](https://www.ncbi.nlm.nih.gov/gene/27148):

> This gene encodes a member of the serine/threonine kinase family of enzymes. This family member is similar to a Drosophila protein that plays a key role in the Hedgehog signaling pathway. This human protein is a positive regulator of the GLI zinc-finger transcription factors. Knockout studies of the homologous mouse gene suggest that defects in this human gene may lead to congenital hydrocephalus, possibly due to a functional defect in motile cilia. Because Hedgehog signaling is frequently …

**Accessions** — [HGNC:17209](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17209) · Entrez [27148](https://www.ncbi.nlm.nih.gov/gene/27148) · UniProt [Q9NRP7](https://www.uniprot.org/uniprotkb/Q9NRP7) · Ensembl [ENSG00000163482](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163482)

## Data

Gene col 8699: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8699); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8699, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8699]; `tensor/DDL_lfc|DDL_z.npy` [8699]; `embed/gene_vectors.npy` [8699]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8699 or target_col == 8699). Every well: [[STK36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STK36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
