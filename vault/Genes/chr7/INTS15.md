---
symbol: "INTS15"
type: "gene"
col: 7106
ensembl_id: "ENSG00000146576"
name: "integrator complex subunit 15"
location: "7p22.1"
module: 2
arm: "+"
pooled_cpm: 8.3
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# INTS15

*integrator complex subunit 15* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.96× (z +10.9, q 7e-25, up in 28 of 37 measured lines) ⚠ toxic. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.87× (z +10.6, q 1e-23, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Trametinib (drug)]] 0.5 µM: 0.821× (z -4.0, q 0.039, down in 11 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Orlistat (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0717×); [[Bendamustine (drug)]] 5 µM in 1 line (SW1417 0.218×); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.260×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Silodosin (drug)]] 5 µM in 1 line (SW48 0.110×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ULK3]] (+0.60, fdr 1e-05), [[CCNQ]] (+0.60, fdr 7e-06), [[ABCC10]] (+0.58, fdr 4e-05); moves opposite to [[CD2AP]] (-0.51, fdr 3e-05), [[AK7]] (-0.50, fdr 1e-04), [[CERT1]] (-0.47, fdr 2e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7106.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +10.9 | 7e-25 | 28/37 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +10.6 | 1e-23 | 36/47 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +9.9 | 7e-21 | 32/47 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +7.6 | 5e-12 | 26/47 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +7.4 | 2e-11 | 21/44 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.49×** | +6.7 | 2e-09 | 17/47 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.47×** | +6.5 | 5e-09 | 20/47 (HEC-1-A, AsPC-1, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.38×** | +5.4 | 4e-06 | 7/47 (LoVo, HEC-1-A, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +5.3 | 6e-06 | 19/45 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +5.3 | 8e-06 | 11/46 (SW480, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.25×** | +5.2 | 8e-06 | 17/44 (SK-MEL-2, A498, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.29×** | +4.0 | 0.003 | 10/46 (A-172, BT-474, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **1.23×** | +3.3 | 0.035 | 11/37 (NCI-H23, A-172, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.23×** | +3.3 | 0.036 | 7/44 (PANC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.21×** | +3.2 | 0.058 | 9/47 (A549, C-33 A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.1 | 0.058 | 5/47 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.059 | 9/46 (LoVo, NCI-H23, …) | top dose only |  |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.087 | 2/44 (SHP-77, J82) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7106.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Orlistat (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0717×); [[Bendamustine (drug)]] 5 µM in 1 line (SW1417 0.218×); [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.260×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Silodosin (drug)]] 5 µM in 1 line (SW48 0.110×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 0.5 µM |  | **0.821×** | -4.0 | 0.039 | 11/48 (AsPC-1, NCI-H1792, …) | two highest doses | noisy plate (z scaled) |
| [[Azithromycin (hydrate) (drug)]] 0.5 µM |  | 0.814× | -3.5 | 0.12 | 7/45 (RPMI-7951, SNU-1, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM |  | 0.830× | -3.1 | 0.43 | 6/46 (C32, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7106. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 2 (1 ⚠) | — | [[Orlistat (drug)]] 0.05 µM 0.0717× (z -15.6) |
| [[A498 (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 9.59 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0874× (z -9.0) |
| [[SW1417 (line)]] | alt | 12.9 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.218× (z -9.6) |
| [[SW48 (line)]] | wt | 14.6 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.110× (z -9.2) |
| [[SW480 (line)]] | alt | 9.82 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.99 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7106), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ULK3]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[CCNQ]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ABCC10]] | +0.58 | +0.42 / +0.69 | both halves | 4e-05 |  |
| [[TRIM65]] | +0.58 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SPOUT1]] | +0.56 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[ZNF746]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[MON1A]] | +0.55 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[UBIAD1]] | +0.55 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[CSK]] | +0.55 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[RABIF]] | +0.54 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[ZBTB39]] | +0.54 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ZSCAN32]] | +0.53 | +0.46 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD2AP]] | -0.51 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[AK7]] | -0.50 | -0.32 / -0.41 | both halves | 1e-04 |  |
| [[CERT1]] | -0.47 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[PRDX2]] | -0.47 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[PKIB]] | -0.47 | -0.40 / -0.22 | both halves | 6e-04 |  |
| [[BRWD3]] | -0.46 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[ATP6V1A]] | -0.46 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[DSTN]] | -0.46 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[QKI]] | -0.46 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[MICU1]] | -0.45 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[CYLD]] | -0.45 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[KDM6A]] | -0.44 | -0.31 / -0.52 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.389). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-8.1, -27.2); signed map (-45.5, -14.8). **Vector** length 50.5, 5.66% of its response variance represented; |z| ≥ 3 in 984 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +10.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.1 | +7.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.3 | +6.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.2 | +0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | +3.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.1 | +5.4 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -0.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:6,590,021-6,608,726 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2718; previously C7orf26 |
| Gene groups (HGNC) | Integrator complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96N11](https://www.uniprot.org/uniprotkb/Q96N11) (Integrator complex subunit 15):

> Component of the integrator complex, a multiprotein complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes. The integrator complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the complex terminates transcription by (1) catalyzing dephosphorylation of the C-terminal domain (CTD) of Pol II subunit …

**Summary**, from NCBI Gene [79034](https://www.ncbi.nlm.nih.gov/gene/79034):

> Involved in RNA polymerase II transcription initiation surveillance and regulation of transcription elongation by RNA polymerase II. Part of INTAC complex and integrator complex. Is active in chromosome and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21702](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21702) · Entrez [79034](https://www.ncbi.nlm.nih.gov/gene/79034) · UniProt [Q96N11](https://www.uniprot.org/uniprotkb/Q96N11) · Ensembl [ENSG00000146576](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146576)

## Data

Gene col 7106: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7106); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7106, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7106]; `tensor/DDL_lfc|DDL_z.npy` [7106]; `embed/gene_vectors.npy` [7106]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7106 or target_col == 7106). Every well: [[INTS15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
