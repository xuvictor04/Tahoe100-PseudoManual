---
symbol: "TSR3"
type: "gene"
col: 149
ensembl_id: "ENSG00000007520"
name: "TSR3 ribosome maturation factor"
location: "16p13.3"
module: 12
arm: "+"
pooled_cpm: 10.52
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# TSR3

*TSR3 ribosome maturation factor* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.19× (z +9.9, q 3e-20, up in 30 of 32 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 4.45×, J82 5.01×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.312× (z -9.8, q 4e-20, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SURF2]] (+0.71, fdr 3e-05), [[SSNA1]] (+0.70, fdr 1e-05), [[NDUFB10]] (+0.68, fdr 1e-05); moves opposite to [[CTSC]] (-0.53, fdr 4e-05), [[TUBA1B]] (-0.50, fdr 4e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 149.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 4.45×, J82 5.01×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.19×** | +9.9 | 3e-20 | 30/32 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.95×** | +8.9 | 2e-16 | 20/20 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +6.0 | 4e-07 | 19/27 (KATO III, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **1.86×** | +5.3 | 2e-05 | 30/41 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.44× | +3.2 | 0.16 | 16/46 (J82, SNU-423, …) | all doses, flat | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.29× | +3.1 | 0.16 | 9/48 (CFPAC-1, HS-578T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.45× | +3.1 | 0.16 | 14/36 (HS-578T, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 1.45× | +3.1 | 0.16 | 16/46 (NCI-H1573, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 149.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.312×** | -9.8 | 4e-20 | 42/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.404×** | -7.7 | 5e-12 | 40/46 (RKO, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.430×** | -7.1 | 2e-10 | 35/46 (hTERT-HPNE, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.478×** | -6.2 | 7e-08 | 34/46 (BT-474, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.627×** | -5.6 | 3e-06 | 28/45 (C-33 A, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.676×** | -4.6 | 3e-04 | 29/48 (A498, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.608×** | -4.2 | 0.002 | 19/43 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.390×** | -4.0 | 0.004 | 24/43 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.622×** | -4.0 | 0.004 | 20/46 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.398×** | -3.9 | 0.005 | 18/47 (LoVo, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Hydroxyurea (drug)]] 5 µM |  | **0.660×** | -3.4 | 0.041 | 13/46 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.658×** | -3.3 | 0.043 | 11/46 (SW480, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 149. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 6.99 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0540× (z -10.3) |
| [[RKO (line)]] | wt | 10.5 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0739× (z -10.0) |
| [[SNU-423 (line)]] | alt | 11.5 | 0 | 2 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0728× (z -11.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.0829× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 9.45 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.117× (z -9.5) |
| [[HOP62 (line)]] | alt | 7.13 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -8.6) |
| [[HT-29 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -9.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0644× (z -11.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 12.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +8.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 7.75 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0549× (z -11.4) |
| [[PANC-1 (line)]] | alt | 14.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 8.64 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.137× (z -10.7) |
| [[A-172 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 149), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 8 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SURF2]] | +0.71 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[SSNA1]] | +0.70 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[NDUFB10]] | +0.68 | +0.64 / +0.52 | both halves | 1e-05 | STRING 406 |
| [[BRMS1]] | +0.66 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[POLR2I]] | +0.65 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[NOL7]] ⚠ | +0.64 | +0.51 / +0.60 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF205]] | +0.62 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[MYG1]] | +0.62 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[STX8]] | +0.62 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[CINP]] | +0.61 | +0.38 / +0.62 | both halves | 6e-05 |  |
| [[RPUSD1]] | +0.61 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[UCK1]] | +0.60 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[PUSL1]] | +0.60 | +0.40 / +0.50 | both halves | 5e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSC]] | -0.53 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[TUBA1B]] | -0.50 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.520). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-44.6, -14.4); signed map (-18.3, -5.9). **Vector** length 55.3, 9.86% of its response variance represented; |z| ≥ 3 in 751 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +1.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | -0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +1.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.6 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.4 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.6 | -9.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -7.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -4.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | +0.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -3.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | TSR3 ribosome maturation factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,349,240-1,351,878 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC24381; previously C16orf42 |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Reactome | 4 pathways, smallest: rRNA modification in the nucleus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UJK0](https://www.uniprot.org/uniprotkb/Q9UJK0) (18S rRNA aminocarboxypropyltransferase):

> Aminocarboxypropyltransferase that catalyzes the aminocarboxypropyl transfer on pseudouridine at position 1248 (Psi1248) in 18S rRNA (Probable). It constitutes the last step in biosynthesis of the hypermodified N1-methyl-N3-(3-amino-3-carboxypropyl) pseudouridine (m1acp3-Psi) conserved in eukaryotic 18S rRNA (Probable).

**Summary**, from NCBI Gene [115939](https://www.ncbi.nlm.nih.gov/gene/115939):

> Enables rRNA small subunit aminocarboxypropyltransferase activity. Involved in enzyme-directed rRNA pseudouridine synthesis. Predicted to be located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:14175](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14175) · Entrez [115939](https://www.ncbi.nlm.nih.gov/gene/115939) · UniProt [Q9UJK0](https://www.uniprot.org/uniprotkb/Q9UJK0) · Ensembl [ENSG00000007520](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000007520)

## Data

Gene col 149: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 149); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 149, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 149]; `tensor/DDL_lfc|DDL_z.npy` [149]; `embed/gene_vectors.npy` [149]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 149 or target_col == 149). Every well: [[TSR3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSR3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
