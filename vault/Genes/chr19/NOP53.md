---
symbol: "NOP53"
type: "gene"
col: 2591
ensembl_id: "ENSG00000105373"
name: "NOP53 ribosome biogenesis factor"
location: "19q13.33"
module: 43
arm: "+"
pooled_cpm: 73.32
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# NOP53

*NOP53 ribosome biogenesis factor* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.59× (z +5.1, q 2e-04, up in 37 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.54× (z +4.8, q 5e-04, up in 38 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Roxadustat (drug)]] 5 µM in 1 line (SW 1271 0.0594×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NACA]] (+0.78, fdr 7e-06, ⚠ NACA in the vector space only through flagged drug-doses), [[EPB41L4A-AS1]] (+0.76, fdr 7e-06), [[RPL21]] (+0.72, fdr 7e-06, ⚠ RPL21 in the vector space only through flagged drug-doses), [[UBXN1]] (+0.72, fdr 7e-06), [[RPL5]] (+0.71, fdr 7e-06); moves opposite to [[SUV39H2]] (-0.63, fdr 7e-06), [[ACTR2]] (-0.57, fdr 2e-05), [[MCM8]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2591.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +5.1 | 2e-04 | 37/49 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +4.8 | 5e-04 | 38/48 (CFPAC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **1.49×** | +4.5 | 0.002 | 39/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.005 | 36/48 (HT-29, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.44×** | +3.9 | 0.013 | 25/43 (A-427, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +3.7 | 0.020 | 30/48 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.4 | 0.052 | 0/50 | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.61×** | +3.4 | 0.054 | 34/47 (LS 180, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.56×** | +3.2 | 0.096 | 30/48 (LS 180, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.33× | +3.1 | 0.10 | 33/47 (HT-29, SW48, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.55× | +3.1 | 0.10 | 28/48 (HT-29, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2591.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Roxadustat (drug)]] 5 µM in 1 line (SW 1271 0.0594×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.800× | -3.0 | 0.95 | 29/48 (HEC-1-A, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2591. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 66.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.86× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 151 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +9.5) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 59.9 | 0 | 1 | — | [[Roxadustat (drug)]] 5 µM 0.0594× (z -9.7) |
| [[A-172 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 78.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 69.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 94.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 83.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 105 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 75.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 79.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 88.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 78.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 68.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 73.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 59.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 68.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 109 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 63.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 91.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 91.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 82.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2591), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 19 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 6 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NACA]] ⚠ | +0.78 | +0.69 / +0.80 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[EPB41L4A-AS1]] | +0.76 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[RPL21]] ⚠ | +0.72 | +0.64 / +0.75 | both halves | 7e-06 | STRING 884; ⚠ in the vector space only through flagged drug-doses |
| [[UBXN1]] | +0.72 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[RPL5]] | +0.71 | +0.59 / +0.76 | both halves | 7e-06 | STRING 992 |
| [[SNHG7]] | +0.70 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[SNHG6]] | +0.68 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[SNHG32]] | +0.68 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[RPS3]] ⚠ | +0.67 | +0.52 / +0.71 | both halves | 1e-05 | STRING 536; ⚠ in the vector space only through flagged drug-doses |
| [[RPL10A]] ⚠ | +0.67 | +0.59 / +0.66 | both halves | 7e-06 | STRING 881; ⚠ in the vector space only through flagged drug-doses |
| [[RPL37]] ⚠ | +0.67 | +0.56 / +0.70 | both halves | 1e-05 | STRING 895; ⚠ in the vector space only through flagged drug-doses |
| [[RPS6]] ⚠ | +0.66 | +0.57 / +0.68 | both halves | 1e-05 | STRING 579; ⚠ in the vector space only through flagged drug-doses |
| [[RPS15A]] | +0.65 | +0.52 / +0.75 | both halves | 1e-05 |  |
| [[ATP5MC2]] | +0.65 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[NSA2]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 | same gene group; STRING 954 |
| [[BTF3]] | +0.63 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[RPL19]] | +0.63 | +0.47 / +0.68 | both halves | 2e-05 | STRING 905 |
| [[RPL34]] | +0.63 | +0.47 / +0.69 | both halves | 2e-05 | STRING 865 |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUV39H2]] | -0.63 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[ACTR2]] | -0.57 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[MCM8]] | -0.56 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[EIF5A]] | -0.55 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[PSME3]] | -0.54 | -0.38 / -0.55 | both halves | 6e-05 |  |
| [[CLSPN]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ARPC5]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[RANBP1]] | -0.53 | -0.50 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.654). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-42.0, -28.8); signed map (-58.4, -6.1). **Vector** length 87.9, 28.0% of its response variance represented; |z| ≥ 3 in 530 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.56 to 55); *Peptide chain elongation* (reactome, mean cos +0.56 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.55 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +1.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +3.5 | +2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | +2.8 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +3.0 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +2.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.8 | +1.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.6 | +3.2 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.6 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -0.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | -1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.5 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.6 | -2.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.2 | -1.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -1.2 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | NOP53 ribosome biogenesis factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:47,745,546-47,757,058 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PICT-1, PICT1; previously GLTSCR2 |
| Gene groups (HGNC) | Ribosome biogenesis factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZM5](https://www.uniprot.org/uniprotkb/Q9NZM5) (Ribosome biogenesis protein NOP53):

> Nucleolar protein which is involved in the integration of the 5S RNP into the ribosomal large subunit during ribosome biogenesis. In ribosome biogenesis, may also play a role in rRNA transcription. Also functions as a nucleolar sensor that regulates the activation of p53/TP53 in response to ribosome biogenesis perturbation, DNA damage and other stress conditions. DNA damage or perturbation of ribosome biogenesis disrupt the interaction between NOP53 and RPL11 allowing RPL11 transport to the …

**Summary**, from NCBI Gene [29997](https://www.ncbi.nlm.nih.gov/gene/29997):

> Enables 5S rRNA binding activity; identical protein binding activity; and p53 binding activity. Involved in several processes, including negative regulation of DNA-templated transcription; regulation of intracellular signal transduction; and regulation of protein metabolic process. Located in cytosol; nuclear lumen; and rDNA heterochromatin. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:4333](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4333) · Entrez [29997](https://www.ncbi.nlm.nih.gov/gene/29997) · UniProt [Q9NZM5](https://www.uniprot.org/uniprotkb/Q9NZM5) · Ensembl [ENSG00000105373](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105373)

## Data

Gene col 2591: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2591); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2591, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2591]; `tensor/DDL_lfc|DDL_z.npy` [2591]; `embed/gene_vectors.npy` [2591]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2591 or target_col == 2591). Every well: [[NOP53 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOP53.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
