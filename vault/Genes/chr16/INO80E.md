---
symbol: "INO80E"
type: "gene"
col: 9820
ensembl_id: "ENSG00000169592"
name: "INO80 complex subunit E"
location: "16p11.2"
module: 5
arm: "+"
pooled_cpm: 21.77
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# INO80E

*INO80 complex subunit E* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.15× (z +11.4, q 4e-27, up in 26 of 33 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (LoVo 4.33×, SW480 2.79×, LS 180 3.37×, PANC-1 2.63×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 5.34×, SW480 3.17×, KATO III 3.20×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.630× (z -7.1, q 6e-10, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SF3A3]] (+0.58, fdr 4e-05), [[CNOT10]] (+0.55, fdr 1e-05), [[SF3A2]] (+0.55, fdr 2e-05); moves opposite to [[MAP1LC3B2]] (-0.54, fdr 5e-05), [[ARL15]] (-0.54, fdr 3e-05), [[GSTP1]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9820.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (LoVo 4.33×, SW480 2.79×, LS 180 3.37×, PANC-1 2.63×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 5.34×, SW480 3.17×, KATO III 3.20×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.15×** | +11.4 | 4e-27 | 26/33 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +11.1 | 5e-26 | 39/42 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.70×** | +7.6 | 6e-12 | 25/38 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +5.9 | 5e-07 | 30/44 (Panc 03.27, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.24× | +3.1 | 0.19 | 16/44 (CFPAC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9820.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.630×** | -7.1 | 6e-10 | 35/48 (C-33 A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.638×** | -6.9 | 1e-09 | 38/48 (J82, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.671×** | -6.2 | 1e-07 | 32/47 (NCI-H2030, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.788×** | -5.2 | 3e-05 | 20/47 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.735×** | -4.8 | 2e-04 | 26/47 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.755×** | -4.3 | 0.001 | 18/48 (HEC-1-A, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.787×** | -3.7 | 0.018 | 11/48 (hTERT-HPNE, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.855× | -3.4 | 0.045 | 17/47 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -3.4 | 0.046 | 20/48 (LS 180, SNU-423, …) | all doses, stronger at high dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.810×** | -3.2 | 0.068 | 11/47 (NCI-H23, NCI-H1573, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.821× | -3.0 | 0.13 | 15/48 (hTERT-HPNE, CHP-212, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9820. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.34× (z +12.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 21.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 26.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -16.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 35.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +9.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 22.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.273× (z -8.5) |
| [[J82 (line)]] | alt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -8.5) |
| [[KATO III (line)]] | alt | 24.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +8.8) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.33× (z +10.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.3) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.63× (z +9.3) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -8.6) |
| [[A-172 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9820), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SF3A3]] | +0.58 | +0.59 / +0.42 | both halves | 4e-05 |  |
| [[CNOT10]] | +0.55 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[SF3A2]] | +0.55 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[DDX51]] | +0.54 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[HAUS5]] | +0.54 | +0.35 / +0.59 | both halves | 1e-04 |  |
| [[PRPF31]] | +0.53 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[HGS]] | +0.52 | +0.40 / +0.52 | both halves | 5e-05 | pathway: Deubiquitination |
| [[MCM3AP]] | +0.52 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[NEURL4]] | +0.51 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[ZC3H18]] | +0.51 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[PES1]] | +0.50 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[USP4]] | +0.50 | +0.43 / +0.51 | both halves | 3e-05 | pathway: Deubiquitination |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAP1LC3B2]] | -0.54 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[ARL15]] | -0.54 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[GSTP1]] | -0.54 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[COX7B]] | -0.52 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[HLA-DRA]] | -0.50 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[LINC00958]] | -0.48 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[SERF2]] | -0.48 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[ETNK1]] | -0.48 | -0.62 / -0.27 | both halves | 3e-04 |  |
| [[HLA-DRB1]] | -0.48 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[PSME1]] | -0.48 | -0.53 / -0.26 | both halves | 4e-04 |  |
| [[PEAK1]] | -0.48 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[HIGD2A]] | -0.48 | -0.45 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.264). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-53.2, -22.9); signed map (-29.4, -51.5). **Vector** length 48.9, 6.77% of its response variance represented; |z| ≥ 3 in 642 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +1.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.7 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +1.6 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.1 | -0.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.1 | +0.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +0.9 | +1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -3.9 | -3.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -2.7 | -3.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.6 | -4.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.3 | -0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | INO80 complex subunit E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:29,995,715-30,005,793 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90652; previously CCDC95 |
| Gene groups (HGNC) | INO80 complex subunits |
| Reactome | 6 pathways, smallest: DNA Damage Recognition in GG-NER; UCH proteinases; Global Genome Nucleotide Excision Repair (GG-NER) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NBZ0](https://www.uniprot.org/uniprotkb/Q8NBZ0) (INO80 complex subunit E):

> Putative regulatory component of the chromatin remodeling INO80 complex which is involved in transcriptional regulation, DNA replication and probably DNA repair.

**Summary**, from NCBI Gene [283899](https://www.ncbi.nlm.nih.gov/gene/283899):

> Involved in several processes, including positive regulation of DNA-templated transcription; regulation of DNA metabolic process; and regulation of chromosome organization. Located in nucleolus and nucleoplasm. Part of Ino80 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26905](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26905) · Entrez [283899](https://www.ncbi.nlm.nih.gov/gene/283899) · UniProt [Q8NBZ0](https://www.uniprot.org/uniprotkb/Q8NBZ0) · Ensembl [ENSG00000169592](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169592)

## Data

Gene col 9820: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9820); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9820, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9820]; `tensor/DDL_lfc|DDL_z.npy` [9820]; `embed/gene_vectors.npy` [9820]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9820 or target_col == 9820). Every well: [[INO80E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INO80E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
