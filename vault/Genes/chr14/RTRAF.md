---
symbol: "RTRAF"
type: "gene"
col: 1500
ensembl_id: "ENSG00000087302"
name: "RNA transcription, translation and transport factor"
location: "14q22.1"
module: 56
arm: "+"
pooled_cpm: 52.28
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# RTRAF

*RNA transcription, translation and transport factor* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.08× (z +8.8, q 7e-16, up in 36 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.39× (z +4.2, q 0.002, up in 30 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRRC1]] (+0.64, fdr 2e-05), [[RWDD1]] (+0.61, fdr 1e-05), [[ACP1]] (+0.61, fdr 3e-05); moves opposite to [[ZNF700]] (-0.52, fdr 1e-04), [[TNPO2]] (-0.51, fdr 1e-04), [[ATF7IP]] (-0.49, fdr 1e-04).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1500.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.08×** | +8.8 | 7e-16 | 36/47 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.73×** | +6.7 | 7e-09 | 31/40 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.66×** | +6.2 | 1e-07 | 37/47 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.50×** | +5.2 | 3e-05 | 33/46 (SW 900, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.70×** | +4.9 | 9e-05 | 32/45 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.27×** | +4.4 | 0.001 | 27/48 (J82, HCT15, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +4.2 | 0.002 | 30/48 (Hs 766T, BT-474, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.012 | 27/48 (NCI-H2030, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +3.7 | 0.012 | 26/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.33×** | +3.6 | 0.015 | 26/48 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.33×** | +3.6 | 0.015 | 23/48 (SK-MEL-2, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.33×** | +3.6 | 0.015 | 25/48 (NCI-H1573, hTERT-HPNE, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.6 | 0.016 | 25/47 (J82, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.32×** | +3.5 | 0.019 | 25/48 (SNU-423, SK-MEL-2, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.023 | 23/48 (Hs 766T, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.024 | 24/48 (CFPAC-1, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +3.3 | 0.031 | 22/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.18× | +2.9 | 0.086 | 13/49 (HT-29, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1500.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pemetrexed (drug)]] 0.5 µM |  | 0.736× | -3.6 | 0.15 | 28/47 (SW48, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.920× | -3.3 | 0.32 | 1/49 (SW 1271) | inconsistent across doses | noisy plate (z scaled) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.782× | -3.1 | 0.40 | 20/48 (PANC-1, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1500. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 37.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A-172 (line)]] | wt | 26.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[LoVo (line)]] | wt | 59.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[LS 180 (line)]] | wt | 57.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H1792 (line)]] | alt | 50.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SHP-77 (line)]] | alt | 60.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[SNU-423 (line)]] | alt | 35.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A-427 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 71.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 79.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 46.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1500), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRC1]] | +0.64 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[RWDD1]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ACP1]] | +0.61 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[YIPF2]] | +0.60 | +0.39 / +0.57 | both halves | 5e-05 |  |
| [[MED8]] | +0.59 | +0.55 / +0.38 | both halves | 6e-05 |  |
| [[ERLEC1]] | +0.58 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[TXNDC11]] | +0.58 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[SUGT1]] | +0.57 | +0.65 / +0.41 | both halves | 4e-05 |  |
| [[NUBP2]] | +0.57 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[ARL1]] | +0.57 | +0.54 / +0.46 | both halves | 2e-05 |  |
| [[COG6]] | +0.57 | +0.39 / +0.48 | both halves | 6e-05 |  |
| [[OXNAD1]] | +0.57 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF700]] | -0.52 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[TNPO2]] | -0.51 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[ATF7IP]] | -0.49 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[ZBTB40]] | -0.49 | -0.43 / -0.27 | both halves | 3e-04 |  |
| [[SCAMP4]] | -0.48 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[OPA3]] | -0.48 | -0.47 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.531). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.8, -33.7); signed map (-47.5, 9.8). **Vector** length 56.6, 13.3% of its response variance represented; |z| ≥ 3 in 574 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.6 | +3.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.5 | +3.3 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | +1.3 | +1.5 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.2 | +1.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.8 | +2.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +0.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.0 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | RNA transcription, translation and transport factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:51,989,514-52,010,694 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSLIG4, CGI-99, RLLM1, CLE, CLE7, LCRP369, hCLE1; previously C14orf166 |
| Gene groups (HGNC) | tRNA splicing ligase complex |
| Reactome | 3 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y224](https://www.uniprot.org/uniprotkb/Q9Y224) (tRNA-splicing ligase complex subunit RTRAF):

> Accessory subunit of the tRNA-splicing ligase complex that acts by directly joining spliced tRNA halves to mature-sized tRNAs by incorporating the precursor-derived splice junction phosphate into the mature tRNA as a canonical 3',5'-phosphodiester. RNA-binding protein involved in modulation of mRNA transcription by Polymerase II. Could also play a role in RNA transport.; (Microbial infection) In case of infection by influenza virus A (IVA), is involved in viral replication.

**Summary**, from NCBI Gene [51637](https://www.ncbi.nlm.nih.gov/gene/51637):

> Enables RNA binding activity and RNA polymerase II complex binding activity. Involved in negative regulation of protein kinase activity; positive regulation of transcription by RNA polymerase II; and tRNA splicing, via endonucleolytic cleavage and ligation. Located in microtubule cytoskeleton; nucleoplasm; and perinuclear region of cytoplasm. Part of tRNA-splicing ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23169](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23169) · Entrez [51637](https://www.ncbi.nlm.nih.gov/gene/51637) · UniProt [Q9Y224](https://www.uniprot.org/uniprotkb/Q9Y224) · Ensembl [ENSG00000087302](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087302)

## Data

Gene col 1500: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1500); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1500, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1500]; `tensor/DDL_lfc|DDL_z.npy` [1500]; `embed/gene_vectors.npy` [1500]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1500 or target_col == 1500). Every well: [[RTRAF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RTRAF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
