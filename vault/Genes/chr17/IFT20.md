---
symbol: "IFT20"
type: "gene"
col: 3024
ensembl_id: "ENSG00000109083"
name: "intraflagellar transport 20"
location: "17q11.2"
module: 40
arm: "+"
pooled_cpm: 26.9
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# IFT20

*intraflagellar transport 20* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.09× (z +8.6, q 7e-15, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.360× (z -8.5, q 9e-15, down in 46 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 0.05 µM: 0.603× (z -4.0, q 0.019, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[YIPF2]] (+0.76, fdr 7e-06), [[MAX]] (+0.75, fdr 7e-06), [[SELENOK]] (+0.73, fdr 7e-06); moves opposite to [[UTP20]] (-0.68, fdr 7e-06), [[SF3B3]] (-0.66, fdr 1e-05), [[ZKSCAN2]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3024.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +8.6 | 7e-15 | 45/47 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.12×** | +6.3 | 1e-07 | 31/40 (SW480, A-427, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +4.8 | 3e-04 | 33/48 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +4.6 | 7e-04 | 33/43 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +4.1 | 0.004 | 30/47 (NCI-H23, SNU-423, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.65×** | +4.0 | 0.006 | 20/34 (SW480, A-172, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +3.9 | 0.008 | 28/48 (SW480, BT-474, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.046 | 27/48 (NCI-H23, A-172, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.47×** | +3.2 | 0.085 | 21/44 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.45× | +3.1 | 0.11 | 25/48 (MIA PaCa-2, HEC-1-A, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | 1.49× | +3.1 | 0.11 | 20/38 (SW480, NCI-H1792, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3024.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.360×** | -8.5 | 9e-15 | 46/48 (SW48, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.603×** | -4.0 | 0.019 | 29/47 (SW1417, RPMI-7951, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.367×** | -3.8 | 0.024 | 32/47 (NCI-H460, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.396×** | -3.5 | 0.056 | 27/48 (SW480, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3024. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 25.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +11.3) | — |
| [[A549 (line)]] | wt | 32.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +9.3) | — |
| [[LOX-IMVI (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.211× (z -8.9) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 19.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 19.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +10.3) | — |
| [[SW1417 (line)]] | alt | 32.2 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.235× (z -9.0) |
| [[SW48 (line)]] | wt | 44.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.178× (z -9.0) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 22.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3024), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YIPF2]] | +0.76 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[MAX]] | +0.75 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[SELENOK]] | +0.73 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[MXD4]] | +0.72 | +0.54 / +0.80 | both halves | 1e-05 |  |
| [[CCDC186]] | +0.72 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[ERLEC1]] | +0.71 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[TULP3]] | +0.70 | +0.63 / +0.72 | both halves | 7e-06 | STRING 571 |
| [[STX5-DT]] | +0.70 | +0.60 / +0.73 | both halves | 7e-06 |  |
| [[GPR107]] | +0.70 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[KIZ]] | +0.70 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[SRP54]] | +0.70 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[ZFPL1]] | +0.69 | +0.71 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP20]] | -0.68 | -0.59 / -0.73 | both halves | 7e-06 |  |
| [[SF3B3]] | -0.66 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.64 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.64 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[PRRC2A]] | -0.63 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[INTS7]] | -0.63 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[RUVBL1]] | -0.63 | -0.54 / -0.70 | both halves | 1e-05 |  |
| [[C1QBP]] | -0.62 | -0.59 / -0.64 | both halves | 7e-06 |  |
| [[ATIC]] | -0.62 | -0.48 / -0.70 | both halves | 2e-05 |  |
| [[COA7]] | -0.62 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.61 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[IPO9]] | -0.61 | -0.47 / -0.67 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IFT20's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.713). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (8.2, -38.9); signed map (-47.2, 14.3). **Vector** length 98.7, 30.8% of its response variance represented; |z| ≥ 3 in 599 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +8.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +2.4 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[Pasireotide (acetate) (drug)]] 5 µM |  | +1.8 | +2.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.7 | -8.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -2.2 |
|  | [[EX229 (drug)]] 5 µM |  | -4.6 | -2.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.5 | -2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.1 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,328,325-28,335,489 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | IFT-B2 complex |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IY31](https://www.uniprot.org/uniprotkb/Q8IY31) (Intraflagellar transport protein 20 homolog):

> Part of intraflagellar transport (IFT) particles involved in ciliary process assembly. May play a role in the trafficking of ciliary membrane proteins from the Golgi complex to the cilium. Regulates the platelet-derived growth factor receptor-alpha (PDGFRA) signaling pathway. Required for protein stability of E3 ubiquitin ligases CBL and CBLB that mediate ubiquitination and internalization of PDGFRA for proper feedback inhibition of PDGFRA signaling. Essential for male fertility. Plays an …

**Summary**, from NCBI Gene [90410](https://www.ncbi.nlm.nih.gov/gene/90410):

> This gene encodes a intraflagellar transport protein important for intracellular transport. The encoded protein forms part of a complex involved in trafficking of proteins from the Golgi body, including recycling of immune signalling components (Finetti et al., PubMed: 19855387). This gene is part of a complex set of sense-antisense loci that may be co-regulated. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. A pseudogene of this gene is …

**Accessions** — [HGNC:30989](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30989) · Entrez [90410](https://www.ncbi.nlm.nih.gov/gene/90410) · UniProt [Q8IY31](https://www.uniprot.org/uniprotkb/Q8IY31) · Ensembl [ENSG00000109083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109083)

## Data

Gene col 3024: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3024); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3024, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3024]; `tensor/DDL_lfc|DDL_z.npy` [3024]; `embed/gene_vectors.npy` [3024]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3024 or target_col == 3024). Every well: [[IFT20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFT20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
