---
symbol: "NUDT1"
type: "gene"
col: 2738
ensembl_id: "ENSG00000106268"
name: "nudix hydrolase 1"
location: "7p22.3"
module: 67
arm: "+"
pooled_cpm: 7.18
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# NUDT1

*nudix hydrolase 1* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.00× (z +10.8, q 1e-24, up in 28 of 29 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 7.52×, NCI-H460 6.49×, PANC-1 4.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 5.68×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.374× (z -6.6, q 2e-08, down in 27 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (H4 0.141×, KATO III 0.226×, Hs 766T 0.160×, SW480 0.298×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (H4 0.0509×, SW480 0.158×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.180×; ⚠ cell-cycle shift, explains ~38% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPW]] (+0.78, fdr 7e-06), [[RPA3]] (+0.74, fdr 7e-06), [[SPC24]] (+0.73, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2738.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HEC-1-A 7.52×, NCI-H460 6.49×, PANC-1 4.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 5.68×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **5.00×** | +10.8 | 1e-24 | 28/29 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **4.04×** | +9.0 | 4e-17 | 14/15 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **2.79×** | +6.4 | 3e-08 | 21/23 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **2.40×** | +5.9 | 5e-07 | 21/31 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.29×** | +5.4 | 9e-06 | 20/30 (NCI-H2030, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.48×** | +3.8 | 0.017 | 20/47 (RKO, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.38× | +3.0 | 0.19 | 15/41 (NCI-H2347, SNU-423, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2738.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (H4 0.141×, KATO III 0.226×, Hs 766T 0.160×, SW480 0.298×); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (H4 0.0509×, SW480 0.158×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.180×; ⚠ cell-cycle shift, explains ~38% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.374×** | -6.6 | 2e-08 | 27/38 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.573×** | -5.3 | 3e-05 | 29/43 (H4, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.383× | -3.4 | 0.13 | 18/47 (HCT15, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.599× | -3.2 | 0.19 | 14/46 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.633× | -3.1 | 0.23 | 12/44 (NCI-H460, A-427, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2738. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 16.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0509× (z -10.3) |
| [[PANC-1 (line)]] | alt | 14.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.68× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | — |
| [[SW480 (line)]] | alt | 9.20 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -9.4) |
| [[HEC-1-A (line)]] | alt | 7.75 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.52× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[Hs 766T (line)]] | wt | 6.80 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -8.9) |
| [[KATO III (line)]] | alt | 11.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 6.11 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | — |
| [[SHP-77 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.180× (z -9.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2738), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPW]] | +0.78 | +0.78 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[RPA3]] | +0.74 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[SPC24]] | +0.73 | +0.82 / +0.63 | both halves | 7e-06 |  |
| [[RAD54L]] | +0.73 | +0.83 / +0.59 | both halves | 7e-06 |  |
| [[GINS2]] | +0.73 | +0.76 / +0.64 | both halves | 7e-06 |  |
| [[UBE2T]] | +0.71 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[CMC2]] | +0.70 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[STIL]] | +0.70 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[HMGB1P5]] ⚠ | +0.69 | +0.57 / +0.72 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[HAT1]] | +0.69 | +0.79 / +0.51 | both halves | 1e-05 |  |
| [[BLM]] | +0.69 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[RFC4]] | +0.68 | +0.71 / +0.57 | both halves | 1e-05 |  |
| [[SNRNP25]] | +0.68 | +0.56 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-31.2, -50.8); signed map (-42.8, -38.7). **Vector** length 51.9, 9.14% of its response variance represented; |z| ≥ 3 in 645 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.61 to 12); *G2/M checkpoint* (hallmark, mean cos +0.60 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.58 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +2.6 | +10.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +2.3 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +2.2 | +9.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.1 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.0 | +2.0 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | +1.0 | +0.8 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.0 | +0.7 |
|  | [[Flutamide (drug)]] 5 µM |  | +0.9 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -6.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -3.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -2.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | nudix hydrolase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:2,242,226-2,251,146 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MTH1 |
| Gene groups (HGNC) | Nudix hydrolase family |
| Reactome | 4 pathways, smallest: Phosphate bond hydrolysis by NUDT proteins; Purine catabolism; Nucleotide catabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P36639](https://www.uniprot.org/uniprotkb/P36639) (Oxidized purine nucleoside triphosphate hydrolase):

> Oxidized purine nucleoside triphosphate hydrolase which is a prominent sanitizer of the oxidized nucleotide pool. Catalyzes the hydrolysis of 2-oxo-dATP (2-hydroxy-dATP) into 2-oxo-dAMP. Also has a significant hydrolase activity toward 2-oxo-ATP, 8-oxo-dGTP and 8-oxo-dATP. Through the hydrolysis of oxidized purine nucleoside triphosphates, prevents their incorporation into DNA and the subsequent transversions A:T to C:G and G:C to T:A. Also catalyzes the hydrolysis of methylated purine …

**Summary**, from NCBI Gene [4521](https://www.ncbi.nlm.nih.gov/gene/4521):

> Misincorporation of oxidized nucleoside triphosphates into DNA/RNA during replication and transcription can cause mutations that may result in carcinogenesis or neurodegeneration. The protein encoded by this gene is an enzyme that hydrolyzes oxidized purine nucleoside triphosphates, such as 8-oxo-dGTP, 8-oxo-dATP, 2-hydroxy-dATP, and 2-hydroxy rATP, to monophosphates, thereby preventing misincorporation. The encoded protein is localized mainly in the cytoplasm, with some in the mitochondria, …

**Accessions** — [HGNC:8048](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8048) · Entrez [4521](https://www.ncbi.nlm.nih.gov/gene/4521) · UniProt [P36639](https://www.uniprot.org/uniprotkb/P36639) · Ensembl [ENSG00000106268](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106268)

## Data

Gene col 2738: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2738); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2738, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2738]; `tensor/DDL_lfc|DDL_z.npy` [2738]; `embed/gene_vectors.npy` [2738]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2738 or target_col == 2738). Every well: [[NUDT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
