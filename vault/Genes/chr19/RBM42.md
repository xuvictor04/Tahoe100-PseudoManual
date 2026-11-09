---
symbol: "RBM42"
type: "gene"
col: 4727
ensembl_id: "ENSG00000126254"
name: "RNA binding motif protein 42"
location: "19q13.12"
module: 7
arm: "+"
pooled_cpm: 28.03
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# RBM42

*RNA binding motif protein 42* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.38× (z +8.9, q 3e-16, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.721× (z -4.8, q 0.001, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUL1]] (+0.68, fdr 7e-06), [[TMEM199]] (+0.68, fdr 7e-06), [[IDH3B]] (+0.66, fdr 7e-06); moves opposite to [[PALS2]] (-0.62, fdr 1e-05), [[AHCY]] (-0.60, fdr 1e-05), [[NME2]] (-0.59, fdr 7e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4727.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.38×** | +8.9 | 3e-16 | 45/47 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.34×** | +8.7 | 8e-16 | 38/42 (PANC-1, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.77×** | +8.3 | 2e-14 | 42/47 (A549, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **2.22×** | +7.9 | 6e-13 | 42/48 (HOP62, PANC-1, …) | rises with dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +7.1 | 2e-10 | 39/47 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **2.04×** | +7.0 | 2e-10 | 27/35 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.95×** | +6.9 | 5e-10 | 43/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +5.6 | 1e-06 | 32/43 (MIA PaCa-2, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.68×** | +5.3 | 6e-06 | 30/46 (HOP62, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.64×** | +5.0 | 3e-05 | 29/46 (NCI-H1573, PANC-1, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.94×** | +4.7 | 1e-04 | 26/39 (A498, SW480, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +4.3 | 7e-04 | 1/48 (MIA PaCa-2) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.002 | 27/47 (HT-29, HS-578T, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.73×** | +4.1 | 0.002 | 29/48 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.87×** | +3.9 | 0.003 | 27/47 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.81×** | +3.7 | 0.007 | 27/44 (SW480, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.79×** | +3.7 | 0.009 | 26/47 (NCI-H460, LoVo, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.5 | 0.016 | 24/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.025 | 23/48 (HOP62, PANC-1, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.62×** | +3.0 | 0.062 | 15/48 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.60×** | +2.9 | 0.083 | 11/48 (A498, LOX-IMVI, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +2.8 | 0.099 | 20/48 (J82, Hs 766T, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.57×** | +2.8 | 0.099 | 13/48 (SNU-423, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4727.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.721×** | -4.8 | 0.001 | 33/48 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.701×** | -3.7 | 0.072 | 27/47 (H4, SW 1271, …) | rises with dose | cell-cycle shift (explains ~17% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4727. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 38.7 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +10.2) | — |
| [[PANC-1 (line)]] | alt | 30.1 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +9.2) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.36× (z +9.1) | — |
| [[A-427 (line)]] | wt | 26.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A498 (line)]] | wt | 33.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.0) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[NCI-H460 (line)]] | wt | 21.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.11× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | — |
| [[A-172 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 34.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4727), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUL1]] | +0.68 | +0.71 / +0.58 | both halves | 7e-06 |  |
| [[TMEM199]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[IDH3B]] | +0.66 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[VPS25]] | +0.66 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[DOHH]] | +0.65 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[FAM200A]] | +0.65 | +0.74 / +0.51 | both halves | 1e-05 |  |
| [[METTL18]] | +0.64 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[HCCS]] | +0.61 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[ZNF764]] | +0.61 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[BPTF]] | +0.61 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[EID2]] | +0.60 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[FCF1]] | +0.60 | +0.72 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PALS2]] | -0.62 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[AHCY]] | -0.60 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[NME2]] | -0.59 | -0.69 / -0.38 | both halves | 7e-05 |  |
| [[LPCAT2]] | -0.57 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[METAP1]] | -0.56 | -0.69 / -0.40 | both halves | 5e-05 |  |
| [[MCOLN2]] | -0.56 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[GGCT]] | -0.55 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[LDHB]] | -0.54 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[PODXL2]] | -0.54 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[RPS7]] | -0.54 | -0.61 / -0.40 | both halves | 5e-05 |  |
| [[SGSM1]] | -0.53 | -0.49 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.644). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-40.1, 11.0); signed map (-4.2, -19.8). **Vector** length 75.7, 20.9% of its response variance represented; |z| ≥ 3 in 724 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +5.8 | +8.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +8.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.9 | +7.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.5 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.0 | +3.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.9 | +2.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.6 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -4.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.9 | -3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -1.2 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -2.0 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -2.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein 42 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,629,030-35,637,686 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10433 |
| Gene groups (HGNC) | RNA binding motif containing; tri-snRP complex |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BTD8](https://www.uniprot.org/uniprotkb/Q9BTD8) (RNA-binding protein 42):

> Binds (via the RRM domain) to the 3'-untranslated region (UTR) of CDKN1A mRNA.

**Summary**, from NCBI Gene [79171](https://www.ncbi.nlm.nih.gov/gene/79171):

> Enables RNA binding activity. Predicted to be involved in spliceosomal snRNP assembly. Predicted to act upstream of or within negative regulation of mRNA splicing, via spliceosome. Predicted to be located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28117](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28117) · Entrez [79171](https://www.ncbi.nlm.nih.gov/gene/79171) · UniProt [Q9BTD8](https://www.uniprot.org/uniprotkb/Q9BTD8) · Ensembl [ENSG00000126254](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126254)

## Data

Gene col 4727: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4727); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4727, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4727]; `tensor/DDL_lfc|DDL_z.npy` [4727]; `embed/gene_vectors.npy` [4727]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4727 or target_col == 4727). Every well: [[RBM42 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBM42.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
