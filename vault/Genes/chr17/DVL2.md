---
symbol: "DVL2"
type: "gene"
col: 59
ensembl_id: "ENSG00000004975"
name: "dishevelled segment polarity protein 2"
location: "17p13.1"
module: 122
arm: "+"
pooled_cpm: 14.92
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# DVL2

*dishevelled segment polarity protein 2* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.43× (z +8.5, q 8e-15, up in 28 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.826× (z -4.7, q 0.002, down in 17 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPP1]] (+0.61, fdr 8e-06), [[MCOLN1]] (+0.61, fdr 1e-05), [[ATP6AP1]] (+0.60, fdr 1e-05); moves opposite to [[SNRPD1]] (-0.47, fdr 4e-05), [[AGAP9]] (-0.47, fdr 8e-05), [[BTBD10]] (-0.45, fdr 3e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 59.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +8.5 | 8e-15 | 28/46 (COLO 205, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +7.1 | 2e-10 | 25/46 (NCI-H460, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.30×** | +6.4 | 4e-08 | 21/48 (SW480, HOP62, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +5.8 | 7e-07 | 24/47 (SW480, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.34×** | +5.0 | 6e-05 | 18/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.32×** | +4.7 | 3e-04 | 17/48 (RKO, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +4.6 | 4e-04 | 16/47 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.25×** | +3.8 | 0.010 | 13/44 (Panc 03.27, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.010 | 15/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[venetoclax (drug)]] 5 µM |  | **1.51×** | +3.7 | 0.014 | 7/45 (NCI-H460, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.16× | +3.6 | 0.015 | 9/48 (PANC-1, NCI-H23, …) | top dose only | position effect removed |
| [[Berbamine (drug)]] 5 µM |  | 1.16× | +3.5 | 0.022 | 4/48 (HT-29, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.23×** | +3.5 | 0.023 | 14/40 (J82, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.4 | 0.025 | 7/47 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.044 | 6/47 (NCI-H2347, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 59.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.826×** | -4.7 | 0.002 | 17/48 (SW480, BT-474, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.766×** | -4.3 | 0.006 | 16/46 (AsPC-1, RKO, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.859× | -3.7 | 0.037 | 10/48 (CFPAC-1, A549, …) | rises with dose |  |
| [[Sodium Salicylate (drug)]] 0.5 µM |  | **0.809×** | -3.6 | 0.037 | 10/47 (CHP-212, SHP-77, …) | rises with dose |  |
| [[Pemetrexed (drug)]] 5 µM |  | **0.817×** | -3.4 | 0.088 | 6/46 (hTERT-HPNE, NCI-H661, …) | top dose only |  |
| [[vincristine (drug)]] 5 µM |  | 0.706× | -3.1 | 0.17 | 8/43 (hTERT-HPNE, NCI-H460, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 59. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 10.1 | 0 | 2 (1 ⚠) | — | [[Clofarabine (drug)]] 0.05 µM 0.0749× (z -11.3) |
| [[A-427 (line)]] | wt | 23.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.220× (z -11.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[AsPC-1 (line)]] | alt | 8.69 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0595× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 15.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 14.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +11.5) | — |
| [[RPMI-7951 (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 9.78 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM 0.0716× (z -11.6) |
| [[SW1417 (line)]] | alt | 15.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +9.7) | — |
| [[SW48 (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0630× (z -11.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 59), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPP1]] | +0.61 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[MCOLN1]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[ATP6AP1]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CRTC2]] | +0.60 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SLC4A2]] | +0.58 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[CTSA]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SPNS1]] | +0.56 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[GLMP]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[DPP7]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ATN1]] | +0.55 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[AMDHD2]] | +0.55 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[NEU1]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRPD1]] | -0.47 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[AGAP9]] | -0.47 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[BTBD10]] | -0.45 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[PLCXD2]] | -0.45 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[DOCK5]] | -0.45 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.3, -18.3); signed map (-10.3, -21.0). **Vector** length 76.3, 13.1% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.2 | +5.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.2 | +0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +3.2 | +6.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.2 | +3.8 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | +2.9 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.8 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | dishevelled segment polarity protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:7,225,342-7,234,517 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Dishevelled segment polarity proteins; PDZ domain containing; DEP domain containing |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING |
| Reactome | 23 pathways, smallest: Negative regulation of TCF-dependent signaling by DVL-interacting proteins; WNT mediated activation of DVL; Killing mechanisms |
| Matched by | ensembl_id |

**Function**, from UniProt [O14641](https://www.uniprot.org/uniprotkb/O14641) (Segment polarity protein dishevelled homolog DVL-2):

> Plays a role in the signal transduction pathways mediated by multiple Wnt genes. Participates both in canonical and non-canonical Wnt signaling by binding to the cytoplasmic C-terminus of frizzled family members and transducing the Wnt signal to down-stream effectors. Promotes internalization and degradation of frizzled proteins upon Wnt signaling.

**Summary**, from NCBI Gene [1856](https://www.ncbi.nlm.nih.gov/gene/1856):

> This gene encodes a member of the dishevelled (dsh) protein family. The vertebrate dsh proteins have approximately 40% amino acid sequence similarity with Drosophila dsh. This gene encodes a 90-kD protein that undergoes posttranslational phosphorylation to form a 95-kD cytoplasmic protein, which may play a role in the signal transduction pathway mediated by multiple Wnt proteins. The mechanisms of dishevelled function in Wnt signaling are likely to be conserved among metazoans. [provided by …

**Accessions** — [HGNC:3086](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3086) · Entrez [1856](https://www.ncbi.nlm.nih.gov/gene/1856) · UniProt [O14641](https://www.uniprot.org/uniprotkb/O14641) · Ensembl [ENSG00000004975](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004975)

## Data

Gene col 59: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 59); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 59, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 59]; `tensor/DDL_lfc|DDL_z.npy` [59]; `embed/gene_vectors.npy` [59]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 59 or target_col == 59). Every well: [[DVL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DVL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
