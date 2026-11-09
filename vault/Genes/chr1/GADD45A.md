---
symbol: "GADD45A"
type: "gene"
col: 3828
ensembl_id: "ENSG00000116717"
name: "growth arrest and DNA damage inducible alpha"
location: "1p31.3"
module: 29
arm: "-"
pooled_cpm: 75.2
n_lines_expressing: 49
n_dd_up: 40
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/029", "written"]
generated_by: "tahoemap"
---

# GADD45A

*growth arrest and DNA damage inducible alpha* — 1p31.3

> [!summary] In one line
> GADD45A is a small stress-inducible nuclear adaptor protein that couples DNA damage and other stresses to G2/M arrest and stress-kinase signalling, and it was one of the first genes shown to be p53-regulated.

## What it is

GADD45A (growth arrest and DNA damage-inducible 45 alpha) is an ~18 kDa acidic nuclear protein, the founding member of a three-gene family with GADD45B and GADD45G. It has no catalytic activity; everything it does, it does by binding partners. It binds PCNA, p21, and the CDK1/cyclin B1 complex, inhibition of which produces G2/M arrest. It binds core histones and has been placed at nucleotide excision repair. And it activates MEKK4/MTK1, feeding the p38 and JNK stress-kinase cascades — which is how a transcriptional stress response becomes a signalling one.

Its induction is promiscuous by design. GADD45A rises after ionising radiation, alkylating agents, UV, hypoxia, oxidative stress and nutrient deprivation. The p53 connection is old and firm: GADD45 was placed in a p53-dependent, ATM-dependent damage-response pathway in the early 1990s, and its p53 response element sits in intron 3 rather than the promoter, one of the examples that taught the field to look inside genes for p53 elements. But the gene is also strongly induced independently of p53, by BRCA1, FOXO3A, ATF4 and octamer- and NF-Y-family factors, and by demethylating agents and HDAC inhibitors. Gadd45a-null mice phenocopy part of p53 loss — genomic instability with aneuploidy and centrosome amplification, increased radiation-induced carcinogenesis, occasional exencephaly — which is the main evidence that it is a real effector rather than a bystander transcript.

GADD45A has a well-developed second life in muscle: it is the ATF4-induced effector required for skeletal muscle atrophy from fasting, immobilisation and denervation, and forcing its expression atrophies myofibres with no upstream stress at all. It has also been proposed to participate in active DNA demethylation with TET and TDG, a claim that has remained contested.

## What is uncertain

The intron 3 response element makes the direct-target status secure, but attributing any particular induction to p53 is less secure here than for any other canonical target in the panel, because the p53-independent inputs are strong and a 379-compound library supplies exactly those inputs — ATF4-driven integrated stress response, oxidative stress, HDAC and methyltransferase inhibition. Whether GADD45A is pro-apoptotic or protective is context-dependent and both have been reported in reputable systems; the arrest function is the better-supported one. The DNA demethylation role should not be assumed. And the muscle work, solid as it is in muscle, says nothing about pooled cancer lines.

## References

- Kastan et al., 1992, Cell — placed GADD45 in a mammalian cell-cycle checkpoint pathway using p53, and showed the pathway is defective in ataxia-telangiectasia.
- Hollander et al., 1999, Nature Genetics — showed Gadd45a-deficient mice have genomic instability, centrosome amplification and increased radiation-induced tumorigenesis, phenocopying parts of p53 loss.
- Ebert et al., 2012, Journal of Biological Chemistry — showed stress-induced Gadd45a is the ATF4 effector required for muscle atrophy from fasting, immobilisation and denervation, and sufficient to cause it alone.
- Tamura et al., 2012, Current Molecular Medicine — review of the GADD45 family in DNA repair, cell-cycle control, senescence and genotoxic stress, including the argument that GADD45 induction is required for the activity of several chemotherapeutic drugs.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (18 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.24× (z +22.3, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Demeclocycline (drug)]] 5 µM: 0.697× (z -4.1, q 0.023, down in 35 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (NCI-H23 0.598×, HOP62 0.609×; ⚠ position not correctable); [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.193×, NCI-H1573 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XPC]] (+0.65, fdr 7e-06), [[ATF4]] (+0.61, fdr 7e-06), [[CEBPB]] (+0.60, fdr 1e-05); moves opposite to [[TUBB]] (-0.58, fdr 1e-05), [[BANF1]] (-0.58, fdr 1e-05), [[DCAF16]] (-0.58, fdr 3e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 18 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3828.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.24×** | +22.3 | 0e+00 | 44/46 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **7.26×** | +15.8 | 0e+00 | 46/46 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **5.84×** | +13.5 | 2e-39 | 45/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **4.66×** | +11.2 | 4e-27 | 39/47 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.40×** | +9.4 | 7e-19 | 42/46 (HepG2/C3A, C32, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **3.07×** | +8.6 | 8e-16 | 40/46 (Hs 766T, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.57×** | +7.5 | 5e-12 | 42/47 (H4, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.51×** | +7.3 | 2e-11 | 41/47 (NCI-H23, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.24×** | +6.4 | 8e-09 | 43/47 (H4, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.11×** | +6.0 | 1e-07 | 35/47 (MIA PaCa-2, PANC-1, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.06×** | +5.8 | 4e-07 | 32/47 (RKO, SNU-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.66×** | +5.7 | 5e-07 | 40/48 (MIA PaCa-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.04×** | +5.3 | 4e-06 | 39/47 (H4, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.57×** | +5.0 | 2e-05 | 29/48 (HOP62, J82, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.83×** | +4.8 | 5e-05 | 34/47 (NCI-H23, HepG2/C3A, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +4.5 | 2e-04 | 35/47 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.68×** | +4.0 | 0.002 | 28/46 (NCI-H23, A-172, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.60×** | +3.6 | 0.008 | 32/47 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.57×** | +3.6 | 0.008 | 30/47 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.37×** | +3.6 | 0.008 | 30/47 (PANC-1, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3828.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (NCI-H23 0.598×, HOP62 0.609×; ⚠ position not correctable); [[Dinaciclib (drug)]] 5 µM in 2 lines (LS 180 0.193×, NCI-H1573 0.153×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Demeclocycline (drug)]] 5 µM |  | **0.697×** | -4.1 | 0.023 | 35/47 (NCI-H23, NCI-H1792, …) | rises with dose | position effect removed |
| [[Pentagastrin (drug)]] 5 µM |  | 0.756× | -3.2 | 0.41 | 26/47 (PANC-1, A-427, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3828. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 133 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +21.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 59.9 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 47.1× (z +21.8) | — |
| [[NCI-H23 (line)]] | alt | 99.2 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +23.0) | [[Adagrasib (drug)]] 0.05 µM 0.598× (z -11.2) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 140 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +20.0) | — |
| [[HepG2_C3A (line)]] | wt | 71.2 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +13.3) | — |
| [[HOP62 (line)]] | alt | 78.6 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 23.2× (z +23.1) | [[Adagrasib (drug)]] 0.05 µM 0.609× (z -8.7) ⚠ position not correctable |
| [[LOX-IMVI (line)]] | wt | 158 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.83× (z +15.3) | — |
| [[NCI-H1573 (line)]] | alt | 47.6 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +18.2) | [[Dinaciclib (drug)]] 5 µM 0.153× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 61.3 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +25.5) | — |
| [[A498 (line)]] | wt | 79.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.9× (z +22.7) | — |
| [[A549 (line)]] | wt | 73.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +20.8) | — |
| [[C32 (line)]] | wt | 57.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +16.3) | — |
| [[Hs 766T (line)]] | wt | 44.6 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +19.1) | — |
| [[hTERT-HPNE (line)]] | wt | 81.5 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +17.2) | — |
| [[RKO (line)]] | wt | 121 | 5 | 0 | [[Harringtonine (drug)]] 0.5 µM 9.04× (z +13.1) | — |
| [[SNU-1 (line)]] | wt | 51.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 11.8× (z +11.8) | — |
| [[A-427 (line)]] | wt | 34.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.07× (z +16.0) | — |
| [[H4 (line)]] | wt | 96.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 78.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.89× (z +18.1) | — |
| [[LS 180 (line)]] | wt | 170 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 34.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.11× (z +15.7) | — |
| [[SW 900 (line)]] | alt | 68.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +14.2) | — |
| [[AsPC-1 (line)]] | alt | 31.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.4× (z +23.2) | — |
| [[HEC-1-A (line)]] | alt | 33.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 42.3 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 22.0× (z +14.1) | — |
| [[NCI-H460 (line)]] | wt | 76.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.05 µM 11.1× (z +10.8) | — |
| [[Panc 03.27 (line)]] | alt | 57.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.92× (z +16.8) | — |
| [[RPMI-7951 (line)]] | alt | 50.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.09× (z +14.9) | — |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +16.6) | — |
| [[SW48 (line)]] | wt | 115 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.71× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 101 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +19.5) | — |
| [[NCI-H1792 (line)]] | alt | 53.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +17.8) | — |
| [[BT-474 (line)]] | alt | 31.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 38.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.26× (z +12.2) | — |
| [[HT-29 (line)]] | alt | 56.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +9.4) | — |
| [[KATO III (line)]] | alt | 44.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +8.6) | — |
| [[LoVo (line)]] | wt | 70.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +16.0) | — |
| [[SW1417 (line)]] | alt | 131 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +11.0) | — |
| [[SW480 (line)]] | alt | 72.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.6) | — |
| [[AN3 CA (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3828), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPC]] | +0.65 | +0.65 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[ATF4]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CEBPB]] | +0.60 | +0.56 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[CDKN1A]] | +0.59 | +0.47 / +0.57 | both halves | 2e-05 | pathway: HALLMARK_APOPTOSIS; STRING 974 |
| [[CCDC174]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[LACC1]] | +0.57 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ABCA12]] | +0.56 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[WASHC1]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[TMEM265]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[RPS27L]] | +0.56 | +0.55 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[CHMP4C]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[ADPRM]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBB]] | -0.58 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[BANF1]] | -0.58 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[DCAF16]] | -0.58 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[RBBP7]] | -0.57 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[MAD2L1]] | -0.57 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[MZT1]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[CALM3]] | -0.56 | -0.64 / -0.37 | both halves | 9e-05 |  |
| [[CNPY3]] | -0.55 | -0.59 / -0.49 | both halves | 2e-05 |  |
| [[LMNB1]] | -0.55 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[AGO1]] | -0.53 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[NAGA]] | -0.52 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[SPC25]] | -0.52 | -0.55 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GADD45A's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.8% of all compounds | 0.013 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PTCHD4]] | B | PTCHD4 activity raises GADD45A's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 1.40× lower at baseline in the lines without PTCHD4 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[PINCR]] | B | PINCR activity raises GADD45A's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.43× lower at baseline in the lines without PINCR | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.500). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-38.2, -31.5); signed map (45.1, -21.6). **Vector** length 102, 37.6% of its response variance represented; |z| ≥ 3 in 1,393 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.9 | +2.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +15.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +5.0 | +3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.7 | +22.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.2 | +5.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.6 | +2.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.2 | +4.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.6 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +1.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | -3.2 | +3.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -1.9 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -0.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -2.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -2.1 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | growth arrest and DNA damage inducible alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:67,685,201-67,688,334 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GADD45; previously DDIT1 |
| Gene groups (HGNC) | Growth arrest and DNA damage inducible family |
| Hallmark sets | APOPTOSIS, EPITHELIAL_MESENCHYMAL_TRANSITION, ADIPOGENESIS, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 5 pathways, smallest: FOXO-mediated transcription of cell cycle genes; TP53 Regulates Transcription of Genes Involved in G2 Cell Cycle Arrest; TP53 Regulates Transcription of Cell Cycle Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P24522](https://www.uniprot.org/uniprotkb/P24522) (Growth arrest and DNA damage-inducible protein GADD45 alpha):

> In T-cells, functions as a regulator of p38 MAPKs by inhibiting p88 phosphorylation and activity (By similarity). Might affect PCNA interaction with some CDK (cell division protein kinase) complexes; stimulates DNA excision repair in vitro and inhibits entry of cells into S phase.

**Summary**, from NCBI Gene [1647](https://www.ncbi.nlm.nih.gov/gene/1647):

> This gene is a member of a group of genes whose transcript levels are increased following stressful growth arrest conditions and treatment with DNA-damaging agents. The protein encoded by this gene responds to environmental stresses by mediating activation of the p38/JNK pathway via MTK1/MEKK4 kinase. The DNA damage-induced transcription of this gene is mediated by both p53-dependent and -independent mechanisms. Alternatively spliced transcript variants encoding distinct isoforms have been …

**Accessions** — [HGNC:4095](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4095) · Entrez [1647](https://www.ncbi.nlm.nih.gov/gene/1647) · UniProt [P24522](https://www.uniprot.org/uniprotkb/P24522) · Ensembl [ENSG00000116717](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116717)

## Data

Gene col 3828: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3828); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3828, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3828]; `tensor/DDL_lfc|DDL_z.npy` [3828]; `embed/gene_vectors.npy` [3828]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3828 or target_col == 3828). Every well: [[GADD45A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/GADD45A.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
