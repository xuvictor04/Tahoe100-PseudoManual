---
symbol: "ENDOV"
type: "gene"
col: 10430
ensembl_id: "ENSG00000173818"
name: "endonuclease V"
location: "17q25.3"
module: 182
arm: "-"
pooled_cpm: 19.95
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/182"]
generated_by: "tahoemap"
---

# ENDOV

*endonuclease V* — 17q25.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.650× (z -5.4, q 2e-05, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR2J4]] (+0.71, fdr 7e-06), [[C19orf25]] (+0.64, fdr 7e-06), [[PROSER3]] (+0.61, fdr 7e-06); moves opposite to [[SLC25A30]] (-0.61, fdr 1e-05), [[PTGFRN]] (-0.58, fdr 1e-05), [[PGM2]] (-0.57, fdr 7e-06).
> It sits in the **-** arm of [[Module 182]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[PNPO]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10430.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.48× | +3.5 | 0.29 | 17/45 (A-427, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.53 | 16/47 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10430.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.650×** | -5.4 | 2e-05 | 30/48 (NCI-H1792, PANC-1, …) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.640×** | -5.4 | 2e-05 | 23/43 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.695×** | -4.6 | 7e-04 | 28/47 (RPMI-7951, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.695×** | -4.6 | 7e-04 | 24/47 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.699×** | -4.5 | 8e-04 | 26/47 (A549, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.704×** | -4.4 | 0.001 | 26/48 (SW480, LOX-IMVI, …) | top dose only | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.516×** | -4.3 | 0.001 | 24/44 (NCI-H1573, SNU-423, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.793×** | -4.1 | 0.003 | 22/47 (A498, Panc 03.27, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.795×** | -4.1 | 0.003 | 23/48 (HOP62, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.726×** | -4.0 | 0.003 | 17/47 (COLO 205, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -3.9 | 0.005 | 22/48 (A-172, C-33 A, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.563×** | -3.8 | 0.008 | 19/48 (hTERT-HPNE, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.748×** | -3.5 | 0.020 | 20/47 (H4, hTERT-HPNE, …) | two highest doses | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.756×** | -3.4 | 0.029 | 18/46 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **0.767×** | -3.3 | 0.034 | 19/48 (SW 1271, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10430. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 25.1 | 0 | 4 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -12.5) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -8.7) |
| [[H4 (line)]] | wt | 30.2 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0759× (z -13.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A498 (line)]] | wt | 20.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -13.3) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A549 (line)]] | wt | 37.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 10.1 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.125× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 0.05 µM 0.0749× (z -10.0) |
| [[HOP62 (line)]] | alt | 28.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.300× (z -9.5) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -8.9) ⚠ cell-cycle shift, explains ~54% of this change |
| [[PANC-1 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.118× (z -9.4) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.312× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 25.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10430), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2J4]] | +0.71 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[C19orf25]] | +0.64 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[PROSER3]] | +0.61 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[MEF2B]] | +0.61 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[GON4L]] | +0.60 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[LAMB2P1]] | +0.58 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[CWC25]] | +0.58 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[OPA3]] | +0.58 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[CHMP1A]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[GCDH]] | +0.57 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[OGG1]] | +0.56 | +0.59 / +0.53 | both halves | 1e-05 | STRING 507 |
| [[ZNF611]] | +0.56 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A30]] | -0.61 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[PTGFRN]] | -0.58 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[PGM2]] | -0.57 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[KDM1A]] | -0.57 | -0.56 / -0.60 | both halves | 1e-05 | same gene group |
| [[COPS6]] | -0.56 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[COX11]] | -0.55 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[FKBP4]] | -0.55 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[STK26]] | -0.54 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[GOLM1]] | -0.54 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[MDH1]] | -0.54 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[TMEM64]] | -0.53 | -0.40 / -0.63 | both halves | 5e-05 |  |
| [[TLCD4]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PNPO]] | C | ENDOV's natural level strengthens PNPO's drug response | ENDOV's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.05; direction not clear | 0.047 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 182]]; 21 genes; this gene is in the **-** arm (projection on the module's main direction -0.612). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-31.9, -14.3); signed map (-18.7, 0.6). **Vector** length 78.2, 15.4% of its response variance represented; |z| ≥ 3 in 781 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.0 | -0.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | -1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.4 | +3.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | +1.8 | +0.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.7 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.1 | -4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -3.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.5 | -5.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -1.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.2 | -3.3 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.8 | -2.4 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.6 | -2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | endonuclease V |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:80,415,165-80,438,086 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35220 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N8Q3](https://www.uniprot.org/uniprotkb/Q8N8Q3) (Endonuclease V):

> [Isoform 1]: Endoribonuclease that specifically cleaves inosine-containing RNAs: cleaves RNA at the second phosphodiester bond 3' to inosine. Active against both single-stranded and double-stranded RNAs. Has strong preference for single-stranded RNAs (ssRNAs) toward double-stranded RNAs (dsRNAs). Cleaves mRNAs and tRNAs containing inosine. Also able to cleave structure-specific dsRNA substrates containing the specific sites 5'-IIUI-3' and 5'-UIUU-3'. Inosine is present in a number of RNAs …

**Summary**, from NCBI Gene [284131](https://www.ncbi.nlm.nih.gov/gene/284131):

> Enables DNA binding activity; RNA endonuclease activity producing 5'-phosphomonoesters, hydrolytic mechanism; and single-stranded RNA binding activity. Predicted to be involved in DNA repair. Located in cytoplasmic stress granule and nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26640](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26640) · Entrez [284131](https://www.ncbi.nlm.nih.gov/gene/284131) · UniProt [Q8N8Q3](https://www.uniprot.org/uniprotkb/Q8N8Q3) · Ensembl [ENSG00000173818](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173818)

## Data

Gene col 10430: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10430); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10430, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10430]; `tensor/DDL_lfc|DDL_z.npy` [10430]; `embed/gene_vectors.npy` [10430]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10430 or target_col == 10430). Every well: [[ENDOV — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENDOV.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
