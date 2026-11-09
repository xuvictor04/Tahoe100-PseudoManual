---
symbol: "MT-ATP6"
type: "gene"
col: 12726
ensembl_id: "ENSG00000198899"
name: "mitochondrially encoded ATP synthase membrane subunit 6"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 500.12
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-ATP6

*mitochondrially encoded ATP synthase membrane subunit 6* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.37× (z +9.7, q 3e-19, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Palmatine (chloride) (drug)]] 5 µM: 1.46× (z +4.4, q 0.001, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.208× (z -13.0, q 1e-35, down in 48 of 48 measured lines) ⚠ transcription drop. The strongest without an alert is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.466× (z -9.0, q 1e-16, down in 42 of 48 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12726.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.37×** | +9.7 | 3e-19 | 44/44 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.83×** | +9.6 | 3e-19 | 49/49 (MIA PaCa-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.58×** | +7.2 | 9e-11 | 45/45 (Panc 03.27, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +6.2 | 6e-08 | 39/47 (KATO III, A-172, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Palmatine (chloride) (drug)]] 5 µM |  | **1.46×** | +4.4 | 0.001 | 34/48 (SW1417, SNU-423, …) | top dose only | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.61×** | +3.9 | 0.008 | 42/49 (SW1417, J82, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.069 | 38/48 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.3 | 0.069 | 33/47 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tranilast (drug)]] 0.5 µM |  | **1.58×** | +3.2 | 0.069 | 39/48 (hTERT-HPNE, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.32×** | +3.2 | 0.069 | 42/48 (MIA PaCa-2, HepG2/C3A, …) | top dose only |  |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | **1.31×** | +3.1 | 0.091 | 28/48 (SW1417, NCI-H2347, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12726.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.208×** | -13.0 | 1e-35 | 48/48 (A-427, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.466×** | -9.0 | 1e-16 | 42/48 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.560×** | -6.8 | 2e-09 | 41/49 (Hs 766T, NCI-H460, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.591×** | -4.4 | 0.002 | 31/48 (LS 180, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.625×** | -3.9 | 0.011 | 31/48 (RKO, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.688× | -3.1 | 0.16 | 31/48 (SW48, C32, …) | top dose only | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.650× | -3.1 | 0.16 | 36/48 (HS-578T, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12726. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 571 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.65× (z +10.1) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.287× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 524 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.87× (z +9.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.212× (z -16.1) |
| [[A-172 (line)]] | wt | 542 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +8.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.269× (z -13.0) |
| [[A-427 (line)]] | wt | 529 | 1 | 3 (1 ⚠) | [[Palmatine (chloride) (drug)]] 5 µM 2.42× (z +8.7) | [[Docetaxel (drug)]] 0.05 µM 0.106× (z -15.6) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.272× (z -12.8) |
| [[HS-578T (line)]] | alt | 393 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +9.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.319× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 411 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.93× (z +10.3) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.275× (z -12.4) |
| [[SNU-423 (line)]] | alt | 513 | 3 (2 ⚠) | 1 (1 ⚠) | [[Palmatine (chloride) (drug)]] 5 µM 2.76× (z +10.1) | [[Docetaxel (drug)]] 0.05 µM 0.274× (z -8.9) ⚠ transcription drop |
| [[A498 (line)]] | wt | 553 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.14× (z +9.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.236× (z -9.8) ⚠ transcription drop |
| [[H4 (line)]] | wt | 331 | 0 | 3 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.287× (z -9.9) |
| [[HOP62 (line)]] | alt | 286 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.31× (z +8.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.252× (z -12.1) |
| [[Hs 766T (line)]] | wt | 473 | 0 | 3 (1 ⚠) | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.266× (z -14.2) |
| [[LOX-IMVI (line)]] | wt | 442 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.87× (z +9.4) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.193× (z -11.8) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 445 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.85× (z +9.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.170× (z -13.2) ⚠ transcription drop |
| [[RKO (line)]] | wt | 692 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.203× (z -9.0) |
| [[AN3 CA (line)]] | alt | 544 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.32× (z +8.6) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.205× (z -9.6) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 562 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.47× (z +8.5) ⚠ toxic | [[Docetaxel (drug)]] 0.05 µM 0.174× (z -12.5) ⚠ transcription drop |
| [[C32 (line)]] | wt | 245 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +8.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.381× (z -8.8) |
| [[COLO 205 (line)]] | alt | 538 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +8.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.179× (z -11.9) ⚠ transcription drop |
| [[HEC-1-A (line)]] | alt | 480 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.66× (z +8.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.254× (z -8.6) ⚠ transcription drop |
| [[HepG2_C3A (line)]] | wt | 367 | 0 | 2 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.351× (z -9.1) |
| [[HT-29 (line)]] | alt | 420 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.97× (z +8.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.203× (z -10.7) ⚠ transcription drop |
| [[KATO III (line)]] | alt | 452 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 4.74× (z +9.1) ⚠ toxic | [[Docetaxel (drug)]] 0.05 µM 0.224× (z -9.1) ⚠ transcription drop |
| [[LoVo (line)]] | wt | 670 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +9.0) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.149× (z -13.1) ⚠ transcription drop |
| [[LS 180 (line)]] | wt | 515 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.243× (z -9.5) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.249× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 418 | 0 | 2 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.296× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 605 | 0 | 2 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.246× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 772 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.155× (z -9.2) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.288× (z -8.7) |
| [[NCI-H661 (line)]] | alt | 384 | 0 | 2 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.239× (z -10.3) |
| [[PANC-1 (line)]] | alt | 525 | 0 | 2 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.236× (z -12.8) |
| [[SW 900 (line)]] | alt | 495 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.162× (z -12.1) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.304× (z -11.2) |
| [[SW1417 (line)]] | alt | 569 | 1 | 1 (1 ⚠) | [[Palmatine (chloride) (drug)]] 5 µM 2.61× (z +10.7) | [[Docetaxel (drug)]] 0.05 µM 0.197× (z -12.8) ⚠ transcription drop |
| [[SW480 (line)]] | alt | 566 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.50× (z +8.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.151× (z -14.0) ⚠ transcription drop |
| [[BT-474 (line)]] | alt | 797 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.162× (z -13.8) ⚠ transcription drop |
| [[C-33 A (line)]] | alt | 365 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.173× (z -9.0) ⚠ transcription drop |
| [[CHP-212 (line)]] | wt | 359 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.56× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 362 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.177× (z -9.5) ⚠ transcription drop |
| [[J82 (line)]] | alt | 399 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.198× (z -13.2) ⚠ transcription drop |
| [[NCI-H1792 (line)]] | alt | 255 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.240× (z -12.7) |
| [[NCI-H2347 (line)]] | alt | 350 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.219× (z -10.3) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 626 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.215× (z -11.2) ⚠ transcription drop |
| [[SK-MEL-2 (line)]] | alt | 1,396 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0739× (z -15.1) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 493 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.229× (z -11.7) |
| [[SW 1271 (line)]] | alt | 413 | 0 | 1 | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.232× (z -11.4) |
| [[SW48 (line)]] | wt | 561 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.191× (z -10.7) ⚠ transcription drop |
| [[CFPAC-1 (line)]] | alt | 308 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 326 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 467 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 532 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 320 | 0 | 0 | — | — |

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
| Name | mitochondrially encoded ATP synthase membrane subunit 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | mitochondria — chrMT:8,527-9,207 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATP6, ATPase-6, Su6m; previously MTATP6, RP |
| Gene groups (HGNC) | Mitochondrial complex V: ATP synthase subunits; Mitochondrially encoded protein coding genes |
| Reactome | 19 pathways, smallest: FASTK family proteins regulate processing and stability of mitochondrial RNAs; Formation of ATP by chemiosmotic coupling; tRNA processing in the mitochondrion |
| Matched by | ensembl_id |

**Function**, from UniProt [P00846](https://www.uniprot.org/uniprotkb/P00846) (ATP synthase F(0) complex subunit a):

> Subunit a, of the mitochondrial membrane ATP synthase complex (F(1)F(0) ATP synthase or Complex V) that produces ATP from ADP in the presence of a proton gradient across the membrane which is generated by electron transport complexes of the respiratory chain (Probable). ATP synthase complex consist of a soluble F(1) head domain - the catalytic core - and a membrane F(1) domain - the membrane proton channel. These two domains are linked by a central stalk rotating inside the F(1) region and a …

**Summary**, from NCBI Gene [4508](https://www.ncbi.nlm.nih.gov/gene/4508):

> Enables proton channel activity. Contributes to proton-transporting ATP synthase activity, rotational mechanism. Involved in proton motive force-driven mitochondrial ATP synthesis and proton transmembrane transport. Located in mitochondrion. Part of proton-transporting ATP synthase complex. Implicated in Leber hereditary optic neuropathy; NARP syndrome; Parkinson's disease; multiple sclerosis; and systemic lupus erythematosus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7414](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7414) · Entrez [4508](https://www.ncbi.nlm.nih.gov/gene/4508) · UniProt [P00846](https://www.uniprot.org/uniprotkb/P00846) · Ensembl [ENSG00000198899](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198899)

## Data

Gene col 12726: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12726); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12726, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12726]; `tensor/DDL_lfc|DDL_z.npy` [12726]; `embed/gene_vectors.npy` [12726]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12726 or target_col == 12726). Every well: [[MT-ATP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-ATP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
