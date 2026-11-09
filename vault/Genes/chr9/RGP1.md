---
symbol: "RGP1"
type: "gene"
col: 2832
ensembl_id: "ENSG00000107185"
name: "RGP1 partner of RAB6A GEF complex"
location: "9p13.3"
module: 25
arm: "-"
pooled_cpm: 34.3
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# RGP1

*RGP1 partner of RAB6A GEF complex* — 9p13.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.673× (z -7.4, q 6e-11, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GOLGA2]] (+0.66, fdr 7e-06), [[SIRT6]] (+0.62, fdr 1e-05), [[PPP1R13L]] (+0.62, fdr 1e-05); moves opposite to [[FUCA2]] (-0.60, fdr 1e-05), [[GALNT7]] (-0.59, fdr 1e-05), [[PON2]] (-0.58, fdr 1e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2832.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.20× | +3.5 | 0.30 | 11/47 (LS 180, HOP62, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2832.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.673×** | -7.4 | 6e-11 | 28/48 (H4, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.483×** | -7.2 | 2e-10 | 35/47 (MIA PaCa-2, Hs 766T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -6.9 | 9e-10 | 32/48 (AsPC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.898× | -6.9 | 9e-10 | 5/48 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.688×** | -6.7 | 2e-09 | 32/47 (A-427, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.715×** | -6.3 | 3e-08 | 28/48 (H4, HOP62, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.534×** | -6.2 | 6e-08 | 29/48 (SW480, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.720×** | -5.9 | 2e-07 | 28/47 (H4, CHP-212, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.732×** | -5.8 | 3e-07 | 29/48 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.753×** | -5.1 | 2e-05 | 26/48 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.766×** | -5.0 | 3e-05 | 27/48 (SK-MEL-2, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.786×** | -4.5 | 3e-04 | 19/48 (hTERT-HPNE, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.645×** | -4.3 | 7e-04 | 18/33 (SW480, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **0.816×** | -3.8 | 0.006 | 20/47 (KATO III, H4, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.870× | -3.5 | 0.018 | 14/48 (LOX-IMVI, Hs 766T, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.836× | -3.2 | 0.051 | 18/47 (LOX-IMVI, RPMI-7951, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.843× | -3.1 | 0.068 | 14/47 (HT-29, NCI-H2030, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.838× | -3.0 | 0.068 | 11/48 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2832. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 54.1 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.235× (z -10.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 33.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.195× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.306× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 85.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 38.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change |
| [[A-427 (line)]] | wt | 23.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 25.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 61.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 25.3 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0426× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.117× (z -8.6) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.100× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW480 (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.203× (z -9.5) ⚠ toxic |
| [[A-172 (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 37.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2832), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLGA2]] | +0.66 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[SIRT6]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[PPP1R13L]] | +0.62 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[INAFM1]] | +0.61 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ARFIP2]] | +0.60 | +0.57 / +0.59 | both halves | 1e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[DIABLO]] | +0.60 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[GON4L]] | +0.59 | +0.57 / +0.59 | both halves | 8e-06 |  |
| [[NOSIP]] | +0.59 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[POLR2J4]] | +0.58 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[ATG4B]] | +0.58 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[SH3GL1]] | +0.58 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[MAP1S]] | +0.58 | +0.56 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FUCA2]] | -0.60 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[GALNT7]] | -0.59 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[PON2]] | -0.58 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[SUMO3]] | -0.57 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[SCARB2]] | -0.57 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[GOLM1]] | -0.56 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[CRPPA]] | -0.55 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[TMEM123]] | -0.55 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[ARSB]] | -0.54 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[PGRMC1]] | -0.54 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[GTF2I]] | -0.54 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[MFSD14A]] | -0.53 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.416). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-28.2, -16.5); signed map (-16.1, 0.3). **Vector** length 84.3, 16.7% of its response variance represented; |z| ≥ 3 in 830 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +2.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.8 | +2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.0 | +2.6 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +1.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | -7.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.8 | -5.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.3 | -3.0 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | RGP1 partner of RAB6A GEF complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,749,287-35,758,585 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0258 |
| Reactome | 7 pathways, smallest: Intra-Golgi traffic; Retrograde transport at the Trans-Golgi-Network; RAB GEFs exchange GTP for GDP on RABs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92546](https://www.uniprot.org/uniprotkb/Q92546) (RAB6A-GEF complex partner protein 2):

> The RIC1-RGP1 complex acts as a guanine nucleotide exchange factor (GEF), which activates RAB6A by exchanging bound GDP for free GTP and may thereby required for efficient fusion of endosome-derived vesicles with the Golgi compartment. The RIC1-RGP1 complex participates in the recycling of mannose-6-phosphate receptors.

**Summary**, from NCBI Gene [9827](https://www.ncbi.nlm.nih.gov/gene/9827):

> Enables guanyl-nucleotide exchange factor activity and small GTPase binding activity. Involved in negative regulation of protein catabolic process; positive regulation of GTPase activity; and retrograde transport, endosome to Golgi. Located in cytosol and membrane. Part of Ric1-Rgp1 guanyl-nucleotide exchange factor complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21965](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21965) · Entrez [9827](https://www.ncbi.nlm.nih.gov/gene/9827) · UniProt [Q92546](https://www.uniprot.org/uniprotkb/Q92546) · Ensembl [ENSG00000107185](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107185)

## Data

Gene col 2832: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2832); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2832, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2832]; `tensor/DDL_lfc|DDL_z.npy` [2832]; `embed/gene_vectors.npy` [2832]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2832 or target_col == 2832). Every well: [[RGP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
