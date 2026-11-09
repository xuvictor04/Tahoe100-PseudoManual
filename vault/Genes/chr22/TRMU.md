---
symbol: "TRMU"
type: "gene"
col: 1955
ensembl_id: "ENSG00000100416"
name: "tRNA mitochondrial 2-thiouridylase"
location: "22q13.31"
module: 164
arm: "+"
pooled_cpm: 25.7
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# TRMU

*tRNA mitochondrial 2-thiouridylase* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.24× (z +10.5, q 8e-23, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.573× (z -9.2, q 3e-17, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HDHD5]] (+0.68, fdr 7e-06), [[MMS19]] (+0.66, fdr 7e-06), [[POM121]] (+0.65, fdr 1e-05); moves opposite to [[TJP1]] (-0.63, fdr 1e-05), [[LINC00342]] (-0.58, fdr 2e-05), [[SKIL]] (-0.56, fdr 1e-05).
> It is in [[Module 164]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1955.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.24×** | +10.5 | 8e-23 | 38/48 (RKO, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.21×** | +7.0 | 5e-10 | 33/46 (LS 180, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.1 | 6e-05 | 21/48 (A-427, SW48, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +4.4 | 0.001 | 19/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.013 | 19/48 (HOP62, NCI-H23, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.27×** | +3.8 | 0.015 | 14/47 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **1.25×** | +3.6 | 0.028 | 18/45 (RKO, LoVo, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.5 | 0.036 | 1/48 (SW 1088) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.095 | 13/46 (C32, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1955.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.573×** | -9.2 | 3e-17 | 33/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.638×** | -7.7 | 4e-12 | 28/42 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.772×** | -6.3 | 7e-08 | 24/47 (MIA PaCa-2, SNU-423, …) | top dose only | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.722×** | -5.4 | 1e-05 | 19/36 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.750×** | -4.7 | 2e-04 | 22/47 (CHP-212, C-33 A, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.778×** | -4.3 | 0.002 | 21/48 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.773×** | -4.1 | 0.004 | 20/40 (KATO III, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.847× | -4.0 | 0.004 | 17/48 (Hs 766T, A-172, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.829×** | -3.2 | 0.082 | 12/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.877× | -3.2 | 0.082 | 13/48 (RPMI-7951, SW 1088, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1955. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 66.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0386× (z -27.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.266× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -9.3) ⚠ cell-cycle shift, explains ~23% of this change |
| [[NCI-H460 (line)]] | wt | 24.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.315× (z -9.8) |
| [[AN3 CA (line)]] | alt | 33.9 | 0 | 1 | — | [[Pemigatinib (drug)]] 0.05 µM 0.113× (z -8.5) |
| [[CHP-212 (line)]] | wt | 35.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0828× (z -9.0) ⚠ toxic |
| [[HOP62 (line)]] | alt | 37.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.333× (z -9.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -14.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -12.2) ⚠ cell-cycle shift, explains ~23% of this change |
| [[NCI-H1573 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -11.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 32.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.3) ⚠ cell-cycle shift, explains ~23% of this change |
| [[A-172 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 28.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1955), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDHD5]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[MMS19]] | +0.66 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[POM121]] | +0.65 | +0.55 / +0.70 | both halves | 1e-05 | pathway: tRNA processing |
| [[XPNPEP1]] | +0.63 | +0.65 / +0.57 | both halves | 1e-05 |  |
| [[PMS2P3-1]] | +0.63 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[PMS2CL]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[CHSY1]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[UBE2O]] | +0.62 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[POM121C]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 | pathway: tRNA processing |
| [[TRIT1]] | +0.62 | +0.58 / +0.60 | both halves | 7e-06 | pathway: tRNA modification in the mitochondrion; STRING 767 |
| [[DCUN1D5]] | +0.61 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[LONP1]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TJP1]] | -0.63 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[LINC00342]] | -0.58 | -0.49 / -0.56 | both halves | 2e-05 |  |
| [[SKIL]] | -0.56 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[PEAK1]] | -0.55 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ID4]] | -0.53 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[ARAP2]] | -0.53 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[PDLIM5]] | -0.52 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[GNG5]] | -0.51 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[LEPROT]] | -0.51 | -0.52 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.737). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.0, -19.8); signed map (-40.2, 21.3). **Vector** length 98.8, 21.8% of its response variance represented; |z| ≥ 3 in 843 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +10.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.6 | +7.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +4.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.0 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.3 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.8 | -9.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -4.3 | -6.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.1 | -4.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.8 | -4.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.6 | -3.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.1 | -3.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | tRNA mitochondrial 2-thiouridylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:46,330,875-46,357,340 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10140, MTO2, MTU1; previously TRMT |
| Reactome | 3 pathways, smallest: tRNA modification in the mitochondrion; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O75648](https://www.uniprot.org/uniprotkb/O75648) (Mitochondrial tRNA-specific 2-thiouridylase 1):

> Catalyzes the 2-thiolation of uridine at the wobble position (U34) of mitochondrial tRNA(Lys), tRNA(Glu) and tRNA(Gln). Required for the formation of 5-taurinomethyl-2-thiouridine (tm5s2U) of mitochondrial tRNA(Lys), tRNA(Glu), and tRNA(Gln) at the wobble position. ATP is required to activate the C2 atom of the wobble base.

**Summary**, from NCBI Gene [55687](https://www.ncbi.nlm.nih.gov/gene/55687):

> This nuclear gene encodes a mitochondrial tRNA-modifying enzyme. The encoded protein catalyzes the 2-thiolation of uridine on the wobble positions of tRNA(Lys), tRNA(Glu), and tRNA(Gln), resulting in the formation of 5-taurinomethyl-2-thiouridine moieties. Mutations in this gene may cause transient infantile liver failure. Polymorphisms in this gene may also influence the severity of deafness caused by mitochondrial 12S ribosomal RNA mutations. Alternative splicing results in multiple …

**Accessions** — [HGNC:25481](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25481) · Entrez [55687](https://www.ncbi.nlm.nih.gov/gene/55687) · UniProt [O75648](https://www.uniprot.org/uniprotkb/O75648) · Ensembl [ENSG00000100416](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100416)

## Data

Gene col 1955: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1955); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1955, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1955]; `tensor/DDL_lfc|DDL_z.npy` [1955]; `embed/gene_vectors.npy` [1955]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1955 or target_col == 1955). Every well: [[TRMU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
