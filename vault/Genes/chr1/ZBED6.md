---
symbol: "ZBED6"
type: "gene"
col: 15032
ensembl_id: "ENSG00000257315"
name: "zinc finger BED-type containing 6"
location: "1q32.1"
module: 153
arm: "+"
pooled_cpm: 5.09
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# ZBED6

*zinc finger BED-type containing 6* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 3.91× (z +8.4, q 4e-14, up in 43 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.469× (z -6.6, q 2e-08, down in 29 of 38 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RMRP]] (+0.75, fdr 7e-06), [[CNOT3]] (+0.70, fdr 2e-05), [[SF3A1]] (+0.68, fdr 2e-05); moves opposite to [[C16orf91]] (-0.59, fdr 1e-04), [[ADPRS]] (-0.51, fdr 2e-04), [[MRPS12]] (-0.51, fdr 5e-04).
> It is in [[Module 153]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15032.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.91×** | +8.4 | 4e-14 | 43/46 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.37×** | +5.3 | 4e-05 | 30/45 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.23×** | +4.9 | 2e-04 | 26/39 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +4.9 | 2e-04 | 18/30 (LoVo, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +4.4 | 8e-04 | 19/36 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.18×** | +4.4 | 8e-04 | 5/14 (MIA PaCa-2, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **2.06×** | +4.4 | 8e-04 | 27/46 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.84×** | +3.7 | 0.013 | 23/44 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.19×** | +3.7 | 0.013 | 17/41 (NCI-H2347, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.74×** | +3.2 | 0.069 | 15/43 (NCI-H23, H4, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +3.2 | 0.069 | 1/8 (PANC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Baicalin (drug)]] 5 µM |  | **1.45×** | +3.2 | 0.075 | 12/48 (MIA PaCa-2, Panc 03.27, …) | top dose only | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.62×** | +3.1 | 0.091 | 11/41 (SW480, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15032.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.469×** | -6.6 | 2e-08 | 29/38 (A549, HOP62, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.419×** | -5.4 | 2e-05 | 32/44 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.442×** | -5.1 | 8e-05 | 30/47 (HOP62, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.486×** | -4.5 | 0.001 | 27/46 (A498, C32, …) | rises with dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.514×** | -4.1 | 0.004 | 23/45 (COLO 205, HepG2/C3A, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.549×** | -3.6 | 0.030 | 16/38 (HepG2/C3A, C32, …) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **0.538×** | -3.6 | 0.030 | 15/38 (SW 900, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.588×** | -3.3 | 0.069 | 19/46 (HepG2/C3A, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.598×** | -3.2 | 0.088 | 18/45 (A498, A-427, …) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.602×** | -3.2 | 0.090 | 19/44 (HOP62, SNU-423, …) | top dose only |  |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.605×** | -3.1 | 0.093 | 13/44 (C-33 A, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15032. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 5.68 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0844× (z -11.0) |
| [[HOP62 (line)]] | alt | 4.84 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0927× (z -8.9) |
| [[J82 (line)]] | alt | 2.60 | 0 | 1 | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0479× (z -8.5) |
| [[SW 900 (line)]] | alt | 8.74 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0780× (z -8.6) |
| [[A-172 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.28 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15032), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMRP]] | +0.75 | +0.72 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CNOT3]] | +0.70 | +0.46 / +0.70 | both halves | 2e-05 |  |
| [[SF3A1]] | +0.68 | +0.47 / +0.71 | both halves | 2e-05 |  |
| [[BAG6]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[RAB1B]] | +0.67 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ATP13A1]] | +0.67 | +0.39 / +0.74 | both halves | 6e-05 |  |
| [[WASH8P]] ⚠ | +0.66 | +0.45 / +0.72 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MED12]] | +0.65 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[USP19]] | +0.64 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[STRN4]] | +0.63 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[LENG8]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ANAPC2]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ACADVL]] | +0.61 | +0.44 / +0.68 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C16orf91]] | -0.59 | -0.36 / -0.61 | both halves | 1e-04 |  |
| [[ADPRS]] | -0.51 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[MRPS12]] | -0.51 | -0.23 / -0.55 | both halves | 5e-04 |  |
| [[NDUFA7]] | -0.51 | -0.25 / -0.53 | both halves | 4e-04 |  |
| [[NUDT22]] | -0.50 | -0.13 / -0.53 | ⚠ one half (not replicated) | 0.002 |  |
| [[ADGRL3-AS1]] | -0.50 | -0.21 / -0.55 | both halves | 7e-04 |  |
| [[SF3B5]] ⚠ | -0.50 | -0.18 / -0.58 | ⚠ one half (not replicated) | 1e-03 | ⚠ in the vector space only through flagged drug-doses |
| [[RABGEF1P1]] | -0.50 | -0.09 / -0.58 | ⚠ one half (not replicated) | 0.003 |  |
| [[MRPL36]] | -0.49 | -0.25 / -0.54 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.3, -23.6); signed map (-14.5, -33.6). **Vector** length 53.7, 6.96% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.5 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +4.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.4 | +0.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +2.3 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | -0.1 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.4 | +3.2 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +1.2 | +2.0 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +1.1 | +1.3 |
|  | [[Altretamine (drug)]] 0.5 µM |  | +1.1 | +1.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.0 | -4.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.7 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.6 | -3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.5 | -4.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[vincristine (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger BED-type containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:203,795,623-203,854,124 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Zinc fingers BED-type |
| Matched by | ensembl_id |

**Function**, from UniProt [P86452](https://www.uniprot.org/uniprotkb/P86452) (Zinc finger BED domain-containing protein 6):

> Transcriptional repressor which binds to the consensus sequence 5'-GCTCGC-3', transcription regulation may be tissue-specific (By similarity). Regulates the expression of target genes such as: IGF2, PGAP6/TMEM8, ENHO, and PIANP (By similarity). Acts as a transcriptional repressor of growth factor IGF2, thereby negatively regulating postnatal growth of muscles and internal organs, especially in females (By similarity). Negatively regulates myoblast differentiation and myoblast mitochondrial …

**Summary**, from NCBI Gene [100381270](https://www.ncbi.nlm.nih.gov/gene/100381270):

> The protein encoded by this transposon-derived intronless gene is a transcriptional repressor that binds to the consensus sequence 5'-GCTCGC-3'. The encoded protein has been shown to repress IGF2 transcription. This gene is located within the first intron of the ZC3H11A gene. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:33273](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33273) · Entrez [100381270](https://www.ncbi.nlm.nih.gov/gene/100381270) · UniProt [P86452](https://www.uniprot.org/uniprotkb/P86452) · Ensembl [ENSG00000257315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257315)

## Data

Gene col 15032: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15032); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15032, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15032]; `tensor/DDL_lfc|DDL_z.npy` [15032]; `embed/gene_vectors.npy` [15032]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15032 or target_col == 15032). Every well: [[ZBED6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBED6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
