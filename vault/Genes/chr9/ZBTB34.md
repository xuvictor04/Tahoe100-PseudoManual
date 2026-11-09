---
symbol: "ZBTB34"
type: "gene"
col: 10795
ensembl_id: "ENSG00000177125"
name: "zinc finger and BTB domain containing 34"
location: "9q33.3"
module: 15
arm: "+"
pooled_cpm: 16.48
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ZBTB34

*zinc finger and BTB domain containing 34* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.07× (z +6.8, q 5e-09, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.390× (z -11.0, q 3e-25, down in 33 of 39 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SNU-423 0.0924×, SK-MEL-2 0.153×, A549 0.217×, HepG2/C3A 0.0851×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (BT-474 0.0643×, NCI-H2347 0.141×, NCI-H1792 0.114×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0757×; ⚠ cell-cycle shift, explains ~61% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0846×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0801×); [[Ipatasertib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0710×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF250]] (+0.62, fdr 1e-05), [[CAPN10]] (+0.58, fdr 1e-05), [[PIP4K2C]] (+0.58, fdr 1e-05); moves opposite to [[THOC2]] (-0.53, fdr 7e-05), [[MYCBP2]] (-0.49, fdr 3e-05), [[LINC01473]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10795.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.07×** | +6.8 | 5e-09 | 36/48 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.39×** | +5.3 | 3e-05 | 28/45 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 1.34× | +3.4 | 0.14 | 14/48 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 1.31× | +3.1 | 0.23 | 18/47 (BT-474, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | 1.32× | +3.1 | 0.23 | 17/44 (SNU-1, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10795.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SNU-423 0.0924×, SK-MEL-2 0.153×, A549 0.217×, HepG2/C3A 0.0851×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (BT-474 0.0643×, NCI-H2347 0.141×, NCI-H1792 0.114×; ⚠ toxic; transcription drop); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.0757×; ⚠ cell-cycle shift, explains ~61% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0846×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0801×); [[Ipatasertib (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.0710×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.390×** | -11.0 | 3e-25 | 33/39 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.502×** | -7.7 | 3e-12 | 25/29 (BT-474, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Arbutin (drug)]] 5 µM |  | 0.761× | -3.1 | 0.42 | 14/47 (C-33 A, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10795. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 15.0 | 0 | 3 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0876× (z -13.4) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ipatasertib (drug)]] 0.5 µM 0.0710× (z -9.1) |
| [[A-172 (line)]] | wt | 26.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -9.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 19.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.314× (z -8.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 31.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0643× (z -16.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 24.4 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0757× (z -14.6) ⚠ cell-cycle shift, explains ~61% of this change |
| [[SNU-423 (line)]] | alt | 22.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0924× (z -15.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -10.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -8.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.126× (z -8.8) ⚠ cell-cycle shift, explains ~59% of this change |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0851× (z -10.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0965× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.284× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.114× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -12.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -9.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0846× (z -12.0) |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0801× (z -10.4) |
| [[SW1417 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -9.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10795), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF250]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 | same gene group |
| [[CAPN10]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[PIP4K2C]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CCNY-AS1]] | +0.56 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[FRG1HP]] | +0.56 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ZNF836]] | +0.56 | +0.50 / +0.58 | both halves | 1e-05 | same gene group |
| [[SDHAP4]] | +0.55 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[C8orf76]] | +0.55 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[LINC00115]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[CDS2]] | +0.54 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[ZNF749]] | +0.54 | +0.52 / +0.51 | both halves | 1e-05 | same gene group |
| [[ABHD17A]] | +0.53 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC2]] | -0.53 | -0.37 / -0.53 | both halves | 7e-05 |  |
| [[MYCBP2]] | -0.49 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[LINC01473]] | -0.48 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[PLCB4]] | -0.48 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[BABAM2]] | -0.47 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[WWOX]] | -0.47 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[ATRX]] | -0.46 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[DLG1]] | -0.46 | -0.21 / -0.49 | both halves | 6e-04 |  |
| [[KIAA0586]] | -0.45 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[HES1]] | -0.45 | -0.40 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.449). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-6.7, -21.1); signed map (-38.0, -9.2). **Vector** length 64.8, 10.7% of its response variance represented; |z| ≥ 3 in 820 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | +5.4 | +3.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | +3.9 | +0.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +2.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | +5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +1.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | +0.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Thymol (drug)]] 5 µM |  | -1.5 | -2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.4 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 34 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:126,860,639-126,885,878 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1993, MGC24652, ZNF918 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCN2](https://www.uniprot.org/uniprotkb/Q8NCN2) (Zinc finger and BTB domain-containing protein 34):

> May be a transcriptional repressor.

**Summary**, from NCBI Gene [403341](https://www.ncbi.nlm.nih.gov/gene/403341):

> Predicted to enable DNA-binding transcription repressor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in negative regulation of transcription by RNA polymerase II; regulation of cytokine production; and regulation of immune system process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:31446](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31446) · Entrez [403341](https://www.ncbi.nlm.nih.gov/gene/403341) · UniProt [Q8NCN2](https://www.uniprot.org/uniprotkb/Q8NCN2) · Ensembl [ENSG00000177125](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177125)

## Data

Gene col 10795: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10795); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10795, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10795]; `tensor/DDL_lfc|DDL_z.npy` [10795]; `embed/gene_vectors.npy` [10795]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10795 or target_col == 10795). Every well: [[ZBTB34 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB34.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
