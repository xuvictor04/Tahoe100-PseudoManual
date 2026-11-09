---
symbol: "H2BC4"
type: "gene"
col: 11117
ensembl_id: "ENSG00000180596"
name: "H2B clustered histone 4"
location: "6p22.2"
module: null
arm: null
pooled_cpm: 13.01
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# H2BC4

*H2B clustered histone 4* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.97× (z +21.1, q 0e+00, up in 42 of 44 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +6.7, q 2e-09, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.502× (z -6.1, q 7e-07, down in 26 of 45 measured lines) ⚠ cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.578× (z -5.1, q 6e-05, down in 25 of 44 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 13 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11117.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **4.97×** | +21.1 | 0e+00 | 42/44 (C32, NCI-H2347, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **3.26×** | +10.6 | 1e-23 | 38/46 (C32, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.55×** | +8.0 | 2e-13 | 23/29 (PANC-1, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.29×** | +7.7 | 2e-12 | 28/43 (C32, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +6.8 | 1e-09 | 24/37 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.7 | 2e-09 | 26/46 (KATO III, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.63×** | +6.4 | 1e-08 | 31/48 (A498, A-427, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.93×** | +6.1 | 7e-08 | 28/47 (KATO III, LoVo, …) | rises with dose | composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +5.4 | 4e-06 | 19/48 (SW480, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **1.60×** | +4.4 | 7e-04 | 21/45 (KATO III, LoVo, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **1.59×** | +4.3 | 9e-04 | 17/40 (PANC-1, NCI-H2030, …) | all doses, flat | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.59×** | +4.3 | 9e-04 | 22/47 (LoVo, KATO III, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +3.7 | 0.008 | 5/20 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.44×** | +3.4 | 0.028 | 20/46 (C32, A549, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~30% of this change | **1.45×** | +3.3 | 0.031 | 16/40 (SHP-77, COLO 205, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | **1.29×** | +3.3 | 0.031 | 18/48 (NCI-H2030, PANC-1, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.042 | 13/47 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | **1.39×** | +3.0 | 0.078 | 11/47 (SW480, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11117.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.502×** | -6.1 | 7e-07 | 26/45 (NCI-H1573, SK-MEL-2, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.551×** | -5.6 | 7e-06 | 28/47 (NCI-H1573, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.578×** | -5.1 | 6e-05 | 25/44 (BT-474, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~50% of this change | **0.601×** | -4.6 | 7e-04 | 20/40 (COLO 205, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.604×** | -4.5 | 7e-04 | 21/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.630×** | -4.3 | 0.001 | 18/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.632×** | -4.3 | 0.001 | 22/47 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.629×** | -4.2 | 0.002 | 21/46 (A549, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.683×** | -3.6 | 0.022 | 16/47 (COLO 205, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.684×** | -3.6 | 0.022 | 17/47 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.759×** | -3.5 | 0.029 | 14/48 (KATO III, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.705×** | -3.3 | 0.051 | 17/46 (H4, HT-29, …) | inconsistent across doses | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.793×** | -3.1 | 0.093 | 14/48 (COLO 205, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.82 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11117. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 13.8 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.53× (z +16.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[C32 (line)]] | wt | 8.58 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +17.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[COLO 205 (line)]] | alt | 34.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +9.1) ⚠ cell-cycle shift, explains ~32% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.108× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~50% of this change |
| [[KATO III (line)]] | alt | 13.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.47× (z +15.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.60× (z +9.4) | — |
| [[SW480 (line)]] | alt | 17.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +11.2) ⚠ cell-cycle shift, explains ~32% of this change | [[Bortezomib (drug)]] 5 µM 0.0330× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~53% of this change |
| [[A498 (line)]] | wt | 5.08 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.05× (z +14.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A549 (line)]] | wt | 9.37 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +9.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[AsPC-1 (line)]] | alt | 5.76 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.73× (z +8.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[C-33 A (line)]] | alt | 10.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0675× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 7.32 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +9.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HOP62 (line)]] | alt | 14.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.41× (z +8.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 11.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +10.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HS-578T (line)]] | alt | 4.53 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.67× (z +10.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 7.66 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.75× (z +9.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[J82 (line)]] | alt | 23.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +12.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[LoVo (line)]] | wt | 6.08 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.10× (z +11.8) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[LOX-IMVI (line)]] | wt | 12.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.18× (z +14.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 11.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +9.0) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 6.62 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.50× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 17.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +11.7) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 27.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.88× (z +16.1) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2347 (line)]] | alt | 8.05 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +16.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H460 (line)]] | wt | 7.83 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.85× (z +13.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[Panc 03.27 (line)]] | alt | 43.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +10.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[RPMI-7951 (line)]] | alt | 9.67 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +9.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SHP-77 (line)]] | alt | 9.70 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.05 µM 0.0853× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 12.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +11.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SNU-423 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.101× (z -9.3) ⚠ toxic |
| [[SW 900 (line)]] | alt | 8.79 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +9.3) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[SW1417 (line)]] | alt | 18.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.87× (z +13.5) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.65 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.4 | 0 | 0 | — | — |

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
| Name | H2B clustered histone 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.2 — chr6:26,086,317-26,123,926 (-) |
| Ensembl biotype | protein_coding |
| Also known as | H2B/l, H2B.1; previously H2BFL, HIST1H2BC |
| Gene groups (HGNC) | H2B histones |
| Reactome | 133 pathways, smallest: Replacement of protamines by nucleosomes in the male pronucleus; ChAHP complex assembly; DNA methylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P62807](https://www.uniprot.org/uniprotkb/P62807) (Histone H2B type 1-C/E/F/G/I):

> Core component of nucleosome. Nucleosomes wrap and compact DNA into chromatin, limiting DNA accessibility to the cellular machineries which require DNA as a template. Histones thereby play a central role in transcription regulation, DNA repair, DNA replication and chromosomal stability. DNA accessibility is regulated via a complex set of post-translational modifications of histones, also called histone code, and nucleosome remodeling.; Has broad antibacterial activity. May contribute to the …

**Summary**, from NCBI Gene [8347](https://www.ncbi.nlm.nih.gov/gene/8347):

> Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Two molecules of each of the four core histones (H2A, H2B, H3, and H4) form an octamer, around which approximately 146 bp of DNA is wrapped in repeating units, called nucleosomes. The linker histone, H1, interacts with linker DNA between nucleosomes and functions in the compaction of chromatin into higher order structures. The protein has antibacterial and antifungal …

**Accessions** — [HGNC:4757](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4757) · Entrez [8347](https://www.ncbi.nlm.nih.gov/gene/8347) · UniProt [P62807](https://www.uniprot.org/uniprotkb/P62807) · Ensembl [ENSG00000180596](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180596)

## Data

Gene col 11117: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11117); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11117, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11117]; `tensor/DDL_lfc|DDL_z.npy` [11117]; `embed/gene_vectors.npy` [11117]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11117 or target_col == 11117). Every well: [[H2BC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/H2BC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
