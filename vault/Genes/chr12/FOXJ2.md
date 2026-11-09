---
symbol: "FOXJ2"
type: "gene"
col: 811
ensembl_id: "ENSG00000065970"
name: "forkhead box J2"
location: "12p13.31"
module: 46
arm: "+"
pooled_cpm: 14.68
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 10
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# FOXJ2

*forkhead box J2* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.17× (z +7.8, q 4e-12, up in 11 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.35× (z +4.1, q 0.007, up in 14 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.492× (z -10.2, q 9e-22, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C5orf15]] (+0.65, fdr 1e-05), [[RNF146]] (+0.64, fdr 1e-05), [[SP1]] (+0.63, fdr 3e-05); moves opposite to [[VMP1]] (-0.60, fdr 1e-05), [[STK17A]] (-0.57, fdr 4e-05), [[RRP7BP-1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[STAT5A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 811.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +7.8 | 4e-12 | 11/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +4.7 | 9e-04 | 16/42 (NCI-H2030, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.35×** | +4.1 | 0.007 | 14/47 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.6 | 0.049 | 15/48 (NCI-H23, NCI-H2030, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.049 | 12/47 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.26× | +3.2 | 0.12 | 16/42 (NCI-H23, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 811.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.492×** | -10.2 | 9e-22 | 34/48 (A498, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.529×** | -9.2 | 1e-17 | 34/48 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.687×** | -5.4 | 1e-05 | 22/47 (A-172, A498, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.700×** | -5.1 | 4e-05 | 21/47 (SW480, A498, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.746×** | -4.2 | 0.003 | 14/47 (NCI-H1573, SW1417, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.753×** | -3.8 | 0.014 | 13/33 (Panc 03.27, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.781×** | -3.6 | 0.029 | 16/39 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses | composition shift |
| [[Fumaric acid (drug)]] 0.5 µM |  | **0.783×** | -3.5 | 0.029 | 9/48 (SW 1088, A-427, …) | two highest doses | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.777×** | -3.4 | 0.035 | 9/47 (SW1417, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Acetohexamide (drug)]] 5 µM |  | 0.846× | -3.4 | 0.035 | 11/48 (NCI-H2347, MIA PaCa-2, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.793×** | -3.3 | 0.042 | 8/47 (NCI-H2030, HS-578T, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -3.0 | 0.11 | 12/48 (SNU-1, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 811. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 24.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -9.7) |
| [[HCT15 (line)]] | alt | 15.9 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0750× (z -11.4) ⚠ toxic · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.128× (z -9.4) |
| [[A-427 (line)]] | wt | 42.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.38× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 17.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0642× (z -8.8) |
| [[HT-29 (line)]] | alt | 8.84 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.163× (z -9.1) |
| [[LoVo (line)]] | wt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.236× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.184× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 25.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0670× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[Panc 03.27 (line)]] | alt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 7.85 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +8.5) ⚠ cell-cycle shift, explains ~7% of this change | — |
| [[RKO (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0926× (z -9.0) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.108× (z -9.5) |
| [[A-172 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 811), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C5orf15]] | +0.65 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[RNF146]] | +0.64 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[SP1]] | +0.63 | +0.46 / +0.64 | both halves | 3e-05 | pathway: Adherens junctions interactions |
| [[CFAP418]] | +0.60 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[SIAH1]] | +0.58 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[CDKN1B]] | +0.58 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[JADE2]] | +0.57 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[NFYB]] | +0.56 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[MED12]] | +0.56 | +0.38 / +0.53 | both halves | 7e-05 |  |
| [[SIX4]] | +0.55 | +0.49 / +0.36 | both halves | 1e-04 |  |
| [[CRTC2]] | +0.55 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[INPPL1]] | +0.55 | +0.44 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMP1]] | -0.60 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[STK17A]] | -0.57 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[RRP7BP-1]] | -0.57 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[ASL]] | -0.57 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[GP6-AS1]] | -0.55 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[LRRFIP1]] | -0.55 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[ELOC]] | -0.54 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[POMP]] | -0.54 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[MYO9B]] | -0.53 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[CMIP]] | -0.53 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[TMEM41B]] | -0.52 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[GIPR]] | -0.51 | -0.31 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STAT5A]] | B | STAT5A activity lowers FOXJ2's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 1.70× higher at baseline in the lines without STAT5A | 0.017 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.587). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (17.7, -23.9); signed map (23.9, -19.1). **Vector** length 74.0, 12.4% of its response variance represented; |z| ≥ 3 in 824 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +2.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.6 | +4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +3.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.9 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.1 | +2.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.9 | +1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Erlotinib (drug)]] 5 µM |  | +1.8 | +2.8 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.8 | -10.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.2 | -9.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.9 | -5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.6 | -4.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.1 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -0.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box J2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:8,032,716-8,055,517 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FHX |
| Gene groups (HGNC) | Forkhead boxes |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 9 pathways, smallest: Positive Regulation of CDH1 Gene Transcription; Regulation of CDH1 Gene Transcription; Regulation of CDH1 Expression and Function |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P0K8](https://www.uniprot.org/uniprotkb/Q9P0K8) (Forkhead box protein J2):

> [Isoform FOXJ2.L]: Transcriptional activator. Able to bind to two different type of DNA binding sites. More effective than isoform FOXJ2.S in transcriptional activation. Plays an important role in spermatogenesis, especially in spermatocyte meiosis (By similarity).; [Isoform FOXJ2.S]: Transcriptional activator.

**Summary**, from NCBI Gene [55810](https://www.ncbi.nlm.nih.gov/gene/55810):

> Enables DNA-binding transcription activator activity, RNA polymerase II-specific; RNA polymerase II cis-regulatory region sequence-specific DNA binding activity; and identical protein binding activity. Involved in several processes, including negative regulation of angiogenesis; negative regulation of blood vessel endothelial cell differentiation; and positive regulation of vascular associated smooth muscle cell proliferation. Located in fibrillar center and nucleoplasm. [provided by Alliance …

**Accessions** — [HGNC:24818](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24818) · Entrez [55810](https://www.ncbi.nlm.nih.gov/gene/55810) · UniProt [Q9P0K8](https://www.uniprot.org/uniprotkb/Q9P0K8) · Ensembl [ENSG00000065970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065970)

## Data

Gene col 811: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 811); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 811, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 811]; `tensor/DDL_lfc|DDL_z.npy` [811]; `embed/gene_vectors.npy` [811]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 811 or target_col == 811). Every well: [[FOXJ2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXJ2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
