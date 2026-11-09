---
symbol: "AKIP1"
type: "gene"
col: 9311
ensembl_id: "ENSG00000166452"
name: "A-kinase interacting protein 1"
location: "11p15.4"
module: 17
arm: "+"
pooled_cpm: 9.82
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 10
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# AKIP1

*A-kinase interacting protein 1* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.68× (z +12.9, q 2e-35, up in 16 of 18 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 4.37×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 3.57×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.435× (z -8.6, q 6e-15, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COMMD8]] (+0.57, fdr 3e-05), [[MRPL40]] (+0.55, fdr 6e-05), [[PYURF]] (+0.53, fdr 1e-05); moves opposite to [[ING5]] (-0.48, fdr 7e-05), [[LINC01772]] (-0.46, fdr 5e-05), [[ADGRL1-AS1]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9311.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 4.37×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 3.57×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.68×** | +12.9 | 2e-35 | 16/18 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.23×** | +12.1 | 4e-31 | 28/31 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.76×** | +5.4 | 1e-05 | 16/23 (J82, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +4.9 | 1e-04 | 19/37 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | 1.37× | +3.2 | 0.15 | 14/37 (A-427, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.36× | +3.1 | 0.15 | 10/46 (PANC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9311.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.435×** | -8.6 | 6e-15 | 39/47 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.568×** | -8.2 | 5e-14 | 32/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.460×** | -8.0 | 3e-13 | 32/46 (BT-474, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.524×** | -6.7 | 4e-09 | 32/45 (NCI-H23, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.603×** | -5.2 | 2e-05 | 27/43 (HT-29, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.424×** | -4.6 | 4e-04 | 20/42 (A-427, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.438×** | -4.4 | 7e-04 | 20/45 (Panc 03.27, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Hydroxyurea (drug)]] 5 µM |  | **0.702×** | -3.5 | 0.033 | 12/47 (A498, hTERT-HPNE, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.730×** | -3.2 | 0.078 | 14/45 (SNU-423, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.736×** | -3.1 | 0.093 | 18/44 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9311. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 9.99 | 0 | 4 | — | [[Digitoxin (drug)]] 0.5 µM 0.0757× (z -11.0) |
| [[NCI-H23 (line)]] | alt | 7.14 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0505× (z -12.3) |
| [[NCI-H460 (line)]] | wt | 8.14 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -10.8) |
| [[A-427 (line)]] | wt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -9.7) |
| [[A498 (line)]] | wt | 21.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +9.5) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.115× (z -9.5) ⚠ toxic |
| [[H4 (line)]] | wt | 9.56 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0779× (z -8.6) |
| [[HT-29 (line)]] | alt | 6.08 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0849× (z -9.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 7.32 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 8.12 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -10.5) |
| [[PANC-1 (line)]] | alt | 20.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.37× (z +11.6) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 9.57 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 10.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0537× (z -10.4) |
| [[SNU-423 (line)]] | alt | 10.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0544× (z -12.7) |
| [[SW480 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.301× (z -8.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9311), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD8]] | +0.57 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[MRPL40]] | +0.55 | +0.39 / +0.63 | both halves | 6e-05 |  |
| [[PYURF]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[LRP12]] | +0.50 | +0.45 / +0.30 | both halves | 2e-04 |  |
| [[TM7SF3]] | +0.49 | +0.49 / +0.39 | both halves | 5e-05 |  |
| [[CASP6]] | +0.49 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[CDK8]] | +0.49 | +0.49 / +0.38 | both halves | 7e-05 |  |
| [[HSPA4L]] | +0.48 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[CEPT1]] | +0.48 | +0.35 / +0.53 | both halves | 1e-04 |  |
| [[GNPTAB]] | +0.48 | +0.40 / +0.36 | both halves | 9e-05 |  |
| [[AGTRAP]] | +0.48 | +0.31 / +0.51 | both halves | 2e-04 |  |
| [[CHST3]] | +0.47 | +0.58 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ING5]] | -0.48 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[LINC01772]] | -0.46 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[ADGRL1-AS1]] | -0.45 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[LINC02018]] | -0.45 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[CYTH2]] | -0.44 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[CCNT2-AS1]] | -0.44 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[UBAP1L]] | -0.44 | -0.21 / -0.50 | both halves | 6e-04 |  |
| [[ARL17A]] | -0.44 | -0.32 / -0.44 | both halves | 1e-04 |  |
| [[ARMH4]] | -0.44 | -0.44 / -0.32 | both halves | 1e-04 |  |
| [[LINC01422]] | -0.43 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[CRYGS]] | -0.43 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[ZNF586]] | -0.42 | -0.43 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.357). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-31.5, 22.4); signed map (-25.3, -20.3). **Vector** length 50.1, 7.07% of its response variance represented; |z| ≥ 3 in 776 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.1 | +3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +2.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +0.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +1.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.5 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | -1.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.3 | +1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -6.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.1 | -8.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.0 | -5.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.1 | -0.5 |
|  | [[Tetracycline (hydrochloride) (drug)]] 5 µM |  | -1.1 | -1.4 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | A-kinase interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:8,911,139-8,920,084 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BCA3; previously C11orf17 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ31](https://www.uniprot.org/uniprotkb/Q9NQ31) (A-kinase-interacting protein 1):

> Enhances NF-kappa-B transcriptional activity by regulating the nuclear localization of the NF-kappa-B subunit RELA and promoting the phosphorylation of RELA by PRKACA. Regulates the effect of the cAMP-dependent protein kinase signaling pathway on the NF-kappa-B activation cascade.

**Summary**, from NCBI Gene [56672](https://www.ncbi.nlm.nih.gov/gene/56672):

> This gene encodes a nuclear protein that interacts with protein kinase A catalytic subunit, and regulates the effect of the cAMP-dependent protein kinase signaling pathway on the NF-kappa-B activation cascade. Alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:1170](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1170) · Entrez [56672](https://www.ncbi.nlm.nih.gov/gene/56672) · UniProt [Q9NQ31](https://www.uniprot.org/uniprotkb/Q9NQ31) · Ensembl [ENSG00000166452](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166452)

## Data

Gene col 9311: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9311); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9311, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9311]; `tensor/DDL_lfc|DDL_z.npy` [9311]; `embed/gene_vectors.npy` [9311]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9311 or target_col == 9311). Every well: [[AKIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
