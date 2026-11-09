---
symbol: "H2AC6"
type: "gene"
col: 11116
ensembl_id: "ENSG00000180573"
name: "H2A clustered histone 6"
location: "6p22.2"
module: null
arm: null
pooled_cpm: 45.53
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 15
n_dd_up_clean: 24
n_dd_down_clean: 8
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# H2AC6

*H2A clustered histone 6* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 6.66× (z +30.9, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.395× (z -10.7, q 5e-24, down in 41 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.545× (z -7.0, q 8e-10, down in 34 of 48 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11116.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **6.66×** | +30.9 | 0e+00 | 47/47 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +16.8 | 0e+00 | 46/49 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.73×** | +15.2 | 0e+00 | 43/47 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.21×** | +12.9 | 5e-36 | 43/47 (NCI-H23, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.10×** | +8.2 | 2e-14 | 35/46 (COLO 205, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.92×** | +7.5 | 5e-12 | 34/48 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.88×** | +7.3 | 2e-11 | 39/49 (A-172, Panc 03.27, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +7.2 | 5e-11 | 30/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +6.7 | 1e-09 | 22/48 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.7 | 5e-07 | 30/47 (HOP62, NCI-H23, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.67×** | +5.7 | 6e-07 | 34/48 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +5.4 | 4e-06 | 25/48 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.58×** | +5.1 | 2e-05 | 24/47 (SK-MEL-2, LOX-IMVI, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +5.1 | 2e-05 | 27/48 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 5 µM |  | **1.36×** | +5.1 | 2e-05 | 22/48 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +4.6 | 2e-04 | 23/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.50×** | +4.3 | 5e-04 | 23/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +4.3 | 7e-04 | 21/48 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11116.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.395×** | -10.7 | 5e-24 | 41/48 (A498, SK-MEL-2, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.545×** | -7.0 | 8e-10 | 34/48 (LOX-IMVI, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.557×** | -6.8 | 3e-09 | 36/48 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.415×** | -5.3 | 2e-05 | 27/42 (COLO 205, RPMI-7951, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.620×** | -5.2 | 2e-05 | 28/48 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.651×** | -5.0 | 7e-05 | 27/48 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~81% of this change | **0.670×** | -4.4 | 7e-04 | 22/46 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.711×** | -3.9 | 0.006 | 21/48 (H4, LS 180, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.736×** | -3.5 | 0.026 | 18/48 (A498, SW1417, …) | inconsistent across doses | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.567×** | -3.4 | 0.036 | 19/48 (CFPAC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.736×** | -3.3 | 0.052 | 17/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.762×** | -3.1 | 0.077 | 12/48 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.05 µM |  | **0.747×** | -3.1 | 0.077 | 17/48 (SNU-423, KATO III, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.751×** | -3.1 | 0.089 | 16/48 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.768×** | -3.0 | 0.090 | 10/48 (A498, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.73 per unit of S-phase module lfc, +0.70 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11116. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 74.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +20.7) | — |
| [[HOP62 (line)]] | alt | 27.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +22.0) | — |
| [[NCI-H460 (line)]] | wt | 16.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +25.1) | — |
| [[C32 (line)]] | wt | 21.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.6× (z +26.4) | — |
| [[COLO 205 (line)]] | alt | 125 | 2 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 8.48× (z +13.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.42× (z +11.2) | [[Bortezomib (drug)]] 5 µM 0.0605× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 50.7 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +20.0) | [[Belinostat (drug)]] 0.5 µM 0.224× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.6× (z +18.0) | — |
| [[NCI-H2030 (line)]] | alt | 46.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +16.6) | — |
| [[RPMI-7951 (line)]] | alt | 71.2 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +14.0) | [[Bortezomib (drug)]] 5 µM 0.0489× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.215× (z -9.2) |
| [[A-427 (line)]] | wt | 21.8 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 15.9× (z +13.2) | — |
| [[HEC-1-A (line)]] | alt | 26.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +17.8) | — |
| [[hTERT-HPNE (line)]] | wt | 45.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +18.4) | — |
| [[J82 (line)]] | alt | 59.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +19.5) | — |
| [[KATO III (line)]] | alt | 71.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.35× (z +20.0) | — |
| [[NCI-H2347 (line)]] | alt | 35.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.10× (z +20.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.286× (z -8.5) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 30.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +15.7) | — |
| [[RKO (line)]] | wt | 15.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +16.1) | — |
| [[SK-MEL-2 (line)]] | alt | 71.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +13.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.241× (z -9.7) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 127 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +19.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.286× (z -8.7) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 42.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.62× (z +22.0) | — |
| [[A498 (line)]] | wt | 44.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +11.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.115× (z -10.6) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 18.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +11.7) | — |
| [[BT-474 (line)]] | alt | 19.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.28× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 116 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.338× (z -9.1) ⚠ cell-cycle shift, explains ~66% of this change |
| [[LoVo (line)]] | wt | 17.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +18.8) | — |
| [[LS 180 (line)]] | wt | 66.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.59× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 59.1 | 0 | 2 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.157× (z -12.4) ⚠ cell-cycle shift, explains ~66% of this change |
| [[NCI-H1792 (line)]] | alt | 37.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.66× (z +15.0) | — |
| [[Panc 03.27 (line)]] | alt | 134 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +17.5) | — |
| [[SNU-423 (line)]] | alt | 64.4 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +13.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.246× (z -9.6) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 64.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +11.1) | — |
| [[A549 (line)]] | wt | 28.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +13.6) | — |
| [[C-33 A (line)]] | alt | 23.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.74× (z +12.4) | — |
| [[H4 (line)]] | wt | 34.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +12.7) | — |
| [[HCT15 (line)]] | alt | 26.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 30.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 67.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +12.9) | — |
| [[HS-578T (line)]] | alt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.90× (z +11.8) | — |
| [[HT-29 (line)]] | alt | 31.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.21× (z +16.0) | — |
| [[SHP-77 (line)]] | alt | 32.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 17.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +13.2) | — |
| [[SW 1271 (line)]] | alt | 52.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 40.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +11.2) | — |
| [[SW48 (line)]] | wt | 22.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.5 | 0 | 0 | — | — |

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
| Name | H2A clustered histone 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.2 — chr6:26,124,145-26,139,116 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously H2AFL, HIST1H2AC |
| Gene groups (HGNC) | H2A histones |
| Reactome | 123 pathways, smallest: ChAHP complex assembly; DNA methylation; FXIIa activates plasma kallikrein-kinin system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93077](https://www.uniprot.org/uniprotkb/Q93077) (Histone H2A type 1-C):

> Core component of nucleosome. Nucleosomes wrap and compact DNA into chromatin, limiting DNA accessibility to the cellular machineries which require DNA as a template. Histones thereby play a central role in transcription regulation, DNA repair, DNA replication and chromosomal stability. DNA accessibility is regulated via a complex set of post-translational modifications of histones, also called histone code, and nucleosome remodeling.

**Summary**, from NCBI Gene [8334](https://www.ncbi.nlm.nih.gov/gene/8334):

> Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Two molecules of each of the four core histones (H2A, H2B, H3, and H4) form an octamer, around which approximately 146 bp of DNA is wrapped in repeating units, called nucleosomes. The linker histone, H1, interacts with linker DNA between nucleosomes and functions in the compaction of chromatin into higher order structures. This gene is intronless and encodes a …

**Accessions** — [HGNC:4733](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4733) · Entrez [8334](https://www.ncbi.nlm.nih.gov/gene/8334) · UniProt [Q93077](https://www.uniprot.org/uniprotkb/Q93077) · Ensembl [ENSG00000180573](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180573)

## Data

Gene col 11116: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11116); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11116, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11116]; `tensor/DDL_lfc|DDL_z.npy` [11116]; `embed/gene_vectors.npy` [11116]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11116 or target_col == 11116). Every well: [[H2AC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/H2AC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
