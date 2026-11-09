---
symbol: "MT-ND2"
type: "gene"
col: 12671
ensembl_id: "ENSG00000198763"
name: "mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 2"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 593.95
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 9
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-ND2

*mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 2* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.48× (z +9.8, q 6e-20, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Palmatine (chloride) (drug)]] 5 µM: 1.38× (z +3.7, q 0.019, up in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 14 lines (NCI-H460 4.23×, A498 4.60×, SNU-423 4.51×, HT-29 4.85×, …; ⚠ toxic; transcription drop); [[Palmatine (chloride) (drug)]] 5 µM in 2 lines (BT-474 2.38×, SW1417 2.33×).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.264× (z -10.9, q 8e-25, down in 48 of 48 measured lines) ⚠ transcription drop. The strongest without an alert is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.406× (z -10.4, q 5e-23, down in 44 of 48 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12671.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 14 lines (NCI-H460 4.23×, A498 4.60×, SNU-423 4.51×, HT-29 4.85×, …; ⚠ toxic; transcription drop); [[Palmatine (chloride) (drug)]] 5 µM in 2 lines (BT-474 2.38×, SW1417 2.33×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.48×** | +9.8 | 6e-20 | 44/44 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.20×** | +9.1 | 3e-17 | 49/49 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.11×** | +8.6 | 2e-15 | 45/45 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.1 | 0.005 | 45/47 (NCI-H2347, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.41×** | +3.9 | 0.009 | 47/48 (NCI-H661, Hs 766T, …) | top dose only | position effect removed |
| [[Palmatine (chloride) (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.019 | 30/48 (BT-474, SW1417, …) | top dose only | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.47× | +3.1 | 0.14 | 41/48 (HOP62, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12671.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.264×** | -10.9 | 8e-25 | 48/48 (SHP-77, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.406×** | -10.4 | 5e-23 | 44/48 (A549, PANC-1, …) | top dose only | position effect removed |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.584×** | -6.2 | 9e-08 | 41/49 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.607×** | -4.1 | 0.006 | 33/48 (Hs 766T, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.613×** | -4.0 | 0.007 | 36/48 (RKO, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.652×** | -3.5 | 0.040 | 31/48 (RKO, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.631×** | -3.5 | 0.040 | 47/48 (SHP-77, Panc 03.27, …) | inconsistent across doses |  |
| [[Tomivosertib (drug)]] 5 µM |  | **0.456×** | -3.4 | 0.055 | 42/48 (KATO III, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.655×** | -3.2 | 0.086 | 45/48 (RKO, LoVo, …) | inconsistent across doses |  |
| [[crizotinib (drug)]] 5 µM |  | **0.672×** | -3.1 | 0.099 | 38/48 (HS-578T, SK-MEL-2, …) | top dose only | position effect removed |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.664× | -3.1 | 0.10 | 46/48 (LoVo, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12671. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 514 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.84× (z +10.2) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.176× (z -19.3) |
| [[A498 (line)]] | wt | 751 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.60× (z +10.6) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.256× (z -13.9) |
| [[A549 (line)]] | wt | 739 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.28× (z +10.3) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.140× (z -20.4) |
| [[HOP62 (line)]] | alt | 440 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +9.6) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.210× (z -16.3) |
| [[NCI-H460 (line)]] | wt | 702 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.23× (z +10.8) ⚠ toxic; transcription drop | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.229× (z -16.3) |
| [[H4 (line)]] | wt | 429 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.14× (z +8.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.261× (z -12.3) |
| [[Hs 766T (line)]] | wt | 879 | 0 | 4 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.183× (z -18.3) |
| [[MIA PaCa-2 (line)]] | alt | 487 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.43× (z +9.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.216× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 545 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.12× (z +9.0) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.343× (z -11.1) |
| [[PANC-1 (line)]] | alt | 800 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.95× (z +9.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.157× (z -19.8) |
| [[SW 900 (line)]] | alt | 709 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +8.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.268× (z -14.0) |
| [[SW480 (line)]] | alt | 602 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.36× (z +9.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.307× (z -11.7) |
| [[A-172 (line)]] | wt | 458 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.30× (z +9.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.257× (z -13.3) |
| [[C32 (line)]] | wt | 367 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.72× (z +9.3) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.252× (z -10.3) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.379× (z -10.3) |
| [[LOX-IMVI (line)]] | wt | 429 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.77× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 363 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.72× (z +9.1) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.278× (z -12.7) |
| [[RKO (line)]] | wt | 560 | 0 | 3 | — | [[Digitoxin (drug)]] 0.5 µM 0.233× (z -9.9) |
| [[SNU-423 (line)]] | alt | 687 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.51× (z +10.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.263× (z -9.6) ⚠ transcription drop |
| [[A-427 (line)]] | wt | 977 | 0 | 2 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.257× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 496 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.50× (z +8.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.194× (z -11.6) ⚠ transcription drop |
| [[BT-474 (line)]] | alt | 639 | 1 | 1 (1 ⚠) | [[Palmatine (chloride) (drug)]] 5 µM 2.38× (z +9.7) | [[Docetaxel (drug)]] 0.05 µM 0.307× (z -9.3) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 329 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.20× (z +9.1) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.301× (z -9.7) |
| [[CFPAC-1 (line)]] | alt | 333 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +9.1) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 430 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +9.1) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.218× (z -10.9) ⚠ transcription drop |
| [[HT-29 (line)]] | alt | 456 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.85× (z +10.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.251× (z -9.6) ⚠ transcription drop |
| [[hTERT-HPNE (line)]] | wt | 387 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.99× (z +9.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.266× (z -9.3) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 437 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.15× (z +10.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 838 | 0 | 2 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.218× (z -14.4) |
| [[NCI-H23 (line)]] | alt | 1,292 | 0 | 2 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.241× (z -14.8) |
| [[Panc 03.27 (line)]] | alt | 463 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.86× (z +8.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.291× (z -9.0) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 323 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 7.94× (z +8.8) ⚠ toxic; transcription drop | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.291× (z -10.8) |
| [[SW1417 (line)]] | alt | 595 | 1 | 1 (1 ⚠) | [[Palmatine (chloride) (drug)]] 5 µM 2.33× (z +9.1) | [[Docetaxel (drug)]] 0.05 µM 0.283× (z -9.6) ⚠ transcription drop |
| [[AN3 CA (line)]] | alt | 395 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.86× (z +9.7) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 499 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.220× (z -9.8) ⚠ transcription drop |
| [[HCT15 (line)]] | alt | 318 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.69× (z +8.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 402 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.337× (z -9.8) |
| [[J82 (line)]] | alt | 429 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.265× (z -8.6) ⚠ transcription drop |
| [[KATO III (line)]] | alt | 745 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.263× (z -9.0) ⚠ transcription drop |
| [[LS 180 (line)]] | wt | 537 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.256× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 549 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.216× (z -11.8) ⚠ transcription drop |
| [[NCI-H661 (line)]] | alt | 540 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.250× (z -11.2) |
| [[SHP-77 (line)]] | alt | 816 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.199× (z -13.4) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 829 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.179× (z -12.6) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 534 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 519 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 579 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 324 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 371 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 333 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 585 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | mitochondria — chrMT:4,470-5,511 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ND2, NAD2; previously MTND2 |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase core subunits; Mitochondrially encoded protein coding genes |
| Reactome | 17 pathways, smallest: FASTK family proteins regulate processing and stability of mitochondrial RNAs; tRNA processing in the mitochondrion; Mitochondrial mRNA modification |
| Matched by | ensembl_id |

**Function**, from UniProt [P03891](https://www.uniprot.org/uniprotkb/P03891) (NADH-ubiquinone oxidoreductase chain 2):

> Core subunit of the mitochondrial membrane respiratory chain NADH dehydrogenase (Complex I) which catalyzes electron transfer from NADH through the respiratory chain, using ubiquinone as an electron acceptor. Essential for the catalytic activity and assembly of complex I.

**Summary**, from NCBI Gene [4536](https://www.ncbi.nlm.nih.gov/gene/4536):

> Enables NADH dehydrogenase (ubiquinone) activity. Involved in mitochondrial electron transport, NADH to ubiquinone and mitochondrial respiratory chain complex I assembly. Located in mitochondrial inner membrane. Part of respiratory chain complex I. Implicated in Leber hereditary optic neuropathy; multiple sclerosis; myocardial infarction; neurodegenerative disease (multiple); and urinary bladder cancer. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7456](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7456) · Entrez [4536](https://www.ncbi.nlm.nih.gov/gene/4536) · UniProt [P03891](https://www.uniprot.org/uniprotkb/P03891) · Ensembl [ENSG00000198763](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198763)

## Data

Gene col 12671: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12671); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12671, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12671]; `tensor/DDL_lfc|DDL_z.npy` [12671]; `embed/gene_vectors.npy` [12671]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12671 or target_col == 12671). Every well: [[MT-ND2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-ND2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
