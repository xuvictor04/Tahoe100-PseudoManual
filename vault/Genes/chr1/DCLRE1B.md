---
symbol: "DCLRE1B"
type: "gene"
col: 4010
ensembl_id: "ENSG00000118655"
name: "DNA cross-link repair 1B"
location: "1p13.2"
module: 6
arm: "+"
pooled_cpm: 3.83
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# DCLRE1B

*DNA cross-link repair 1B* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +10.3, q 5e-22, up in 23 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.686× (z -4.4, q 0.005, down in 9 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.101×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (A-172 0.0984×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0728×); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0926×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUV39H1]] (+0.70, fdr 7e-06), [[GINS3]] (+0.70, fdr 7e-06), [[RNASEH2A]] (+0.67, fdr 7e-06); moves opposite to [[TALAM1]] (-0.57, fdr 1e-05), [[STAG3L4-1]] (-0.52, fdr 3e-05), [[ZBTB47-AS1]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4010.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +10.3 | 5e-22 | 23/37 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.93×** | +7.7 | 5e-12 | 22/47 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.87×** | +7.3 | 6e-11 | 19/45 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.87×** | +7.0 | 3e-10 | 10/20 (Panc 03.27, SW480, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.81×** | +6.9 | 5e-10 | 19/44 (HOP62, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.67×** | +6.0 | 2e-07 | 15/46 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.65×** | +5.8 | 5e-07 | 9/21 (A-427, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.51×** | +4.8 | 1e-04 | 9/46 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **1.53×** | +4.8 | 1e-04 | 0/6 | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +4.8 | 1e-04 | 14/44 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +4.2 | 0.001 | 10/43 (PANC-1, SNU-423, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.39×** | +3.8 | 0.006 | 6/35 (LOX-IMVI, NCI-H2347, …) | rises with dose |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.87×** | +3.8 | 0.006 | 2/11 (SW480, A498) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +3.8 | 0.007 | 5/39 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.38×** | +3.7 | 0.008 | 5/46 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.028 | 6/31 (A549, SW480, …) | all doses, flat | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.63×** | +3.0 | 0.090 | 1/21 (HS-578T) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4010.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-172 0.101×; ⚠ cell-cycle shift, explains ~0% of this change); [[Canagliflozin (drug)]] 0.05 µM in 1 line (A-172 0.0984×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0728×); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0926×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.686×** | -4.4 | 0.005 | 9/47 (SNU-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.770× | -3.1 | 0.46 | 10/43 (NCI-H23, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | 0.773× | -3.0 | 0.46 | 2/46 (SNU-423, C-33 A) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.64 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4010. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.43 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Canagliflozin (drug)]] 0.05 µM 0.0984× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 4.25 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.107× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 2.09 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0926× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 5.38 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0728× (z -9.0) |
| [[SW480 (line)]] | alt | 4.44 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4010), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUV39H1]] | +0.70 | +0.73 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[GINS3]] | +0.70 | +0.63 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[RNASEH2A]] | +0.67 | +0.66 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[HASPIN]] | +0.66 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[FEN1]] | +0.65 | +0.49 / +0.74 | both halves | 1e-05 | STRING 527 |
| [[TCF19]] | +0.65 | +0.67 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[FAM111B]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[CDC25A]] | +0.63 | +0.55 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_E2F_TARGETS |
| [[ERCC6L]] | +0.62 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[MCM10]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[E2F2]] | +0.61 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[PKMYT1]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TALAM1]] | -0.57 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[STAG3L4-1]] | -0.52 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ZBTB47-AS1]] | -0.50 | -0.43 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.566). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-38.5, -42.6); signed map (-38.6, -50.1). **Vector** length 50.9, 6.29% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Unwinding of DNA* (reactome, mean cos +0.52 to 12); *Orc1 removal from chromatin* (reactome, mean cos +0.50 to 12); *CDC6 association with the ORC:origin complex* (reactome, mean cos +0.51 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.0 | +6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.3 | +4.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.1 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | +2.0 | +7.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | +1.9 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | +0.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.0 | +2.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -1.6 | -0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.6 | -4.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.4 | -2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | -1.0 | -1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -0.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | DNA cross-link repair 1B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.2 — chr1:113,904,619-113,914,086 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SNM1B, FLJ12810, FLJ13998, APOLLO |
| Gene groups (HGNC) | DNA cross-link repair family |
| Hallmark sets | E2F_TARGETS |
| Reactome | 2 pathways, smallest: Fanconi Anemia Pathway; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H816](https://www.uniprot.org/uniprotkb/Q9H816) (5' exonuclease Apollo):

> 5'-3' exonuclease that plays a central role in telomere maintenance and protection during S-phase. Participates in the protection of telomeres against non-homologous end-joining (NHEJ)-mediated repair, thereby ensuring that telomeres do not fuse. Plays a key role in telomeric loop (T loop) formation by being recruited by TERF2 at the leading end telomeres and by processing leading-end telomeres immediately after their replication via its exonuclease activity: generates 3' single-stranded …

**Summary**, from NCBI Gene [64858](https://www.ncbi.nlm.nih.gov/gene/64858):

> DNA interstrand cross-links prevent strand separation, thereby physically blocking transcription, replication, and segregation of DNA. DCLRE1B is one of several evolutionarily conserved genes involved in repair of interstrand cross-links (Dronkert et al., 2000 [PubMed 10848582]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:17641](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17641) · Entrez [64858](https://www.ncbi.nlm.nih.gov/gene/64858) · UniProt [Q9H816](https://www.uniprot.org/uniprotkb/Q9H816) · Ensembl [ENSG00000118655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000118655)

## Data

Gene col 4010: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4010); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4010, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4010]; `tensor/DDL_lfc|DDL_z.npy` [4010]; `embed/gene_vectors.npy` [4010]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4010 or target_col == 4010). Every well: [[DCLRE1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCLRE1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
