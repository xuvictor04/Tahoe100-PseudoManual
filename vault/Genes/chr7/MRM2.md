---
symbol: "MRM2"
type: "gene"
col: 4364
ensembl_id: "ENSG00000122687"
name: "mitochondrial rRNA methyltransferase 2"
location: "7p22.3"
module: 11
arm: "+"
pooled_cpm: 14.62
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# MRM2

*mitochondrial rRNA methyltransferase 2* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 7.33× (z +11.1, q 7e-26, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (BT-474 0.0859×, A-427 0.126×; ⚠ cell-cycle shift, would explain all of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0988×; ⚠ cell-cycle shift, explains ~76% of this change); [[Pioglitazone (drug)]] 0.5 µM in 1 line (SNU-1 0.0507×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UTP3]] (+0.80, fdr 7e-06), [[CCDC137]] (+0.79, fdr 7e-06), [[SURF6]] (+0.78, fdr 7e-06); moves opposite to [[RTN3]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4364.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **7.33×** | +11.1 | 7e-26 | 46/48 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.94×** | +9.9 | 9e-21 | 37/47 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.43×** | +9.5 | 6e-19 | 41/46 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.49×** | +9.3 | 2e-18 | 36/40 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.35×** | +8.7 | 3e-16 | 43/47 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +8.5 | 2e-15 | 38/46 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.22×** | +8.2 | 2e-14 | 41/47 (NCI-H1792, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.92×** | +7.0 | 2e-10 | 37/48 (AsPC-1, NCI-H1792, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.92×** | +6.9 | 3e-10 | 39/48 (PANC-1, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.74×** | +5.9 | 2e-07 | 33/48 (H4, LOX-IMVI, …) | two highest doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.60×** | +5.0 | 3e-05 | 25/47 (H4, A549, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.39×** | +4.8 | 6e-05 | 25/43 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.57×** | +4.8 | 8e-05 | 24/43 (PANC-1, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.4 | 5e-04 | 23/48 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.50×** | +4.2 | 0.001 | 21/47 (KATO III, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.48×** | +3.9 | 0.004 | 25/44 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.007 | 22/47 (SW480, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4364.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (BT-474 0.0859×, A-427 0.126×; ⚠ cell-cycle shift, would explain all of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.0988×; ⚠ cell-cycle shift, explains ~76% of this change); [[Pioglitazone (drug)]] 0.5 µM in 1 line (SNU-1 0.0507×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sonidegib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.734× | -3.3 | 0.51 | 11/47 (SW480, A549, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4364. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 24.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +10.8) | — |
| [[A-427 (line)]] | wt | 18.4 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0988× (z -12.4) ⚠ cell-cycle shift, explains ~76% of this change |
| [[BT-474 (line)]] | alt | 18.3 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0859× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 10.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +14.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.61× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 16.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.2) | — |
| [[SW480 (line)]] | alt | 22.2 | 2 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.01× (z +11.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 9.95× (z +10.0) | — |
| [[KATO III (line)]] | alt | 24.7 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.45× (z +9.5) ⚠ toxic | — |
| [[SNU-1 (line)]] | wt | 10.0 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0507× (z -10.4) |
| [[A-172 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4364), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP3]] | +0.80 | +0.84 / +0.76 | both halves | 7e-06 | pathway: rRNA processing; STRING 435 |
| [[CCDC137]] | +0.79 | +0.77 / +0.83 | both halves | 7e-06 |  |
| [[SURF6]] | +0.78 | +0.81 / +0.79 | both halves | 7e-06 |  |
| [[TRMT10C]] | +0.74 | +0.77 / +0.71 | both halves | 7e-06 | same gene group; pathway: rRNA processing; STRING 611 |
| [[ZNF75A]] | +0.73 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[RPP14]] | +0.73 | +0.72 / +0.74 | both halves | 7e-06 | pathway: rRNA processing |
| [[THUMPD3]] | +0.73 | +0.76 / +0.66 | both halves | 7e-06 | same gene group |
| [[EID2]] | +0.72 | +0.73 / +0.75 | both halves | 7e-06 |  |
| [[PHAX]] | +0.72 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[ZBTB6]] | +0.72 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[LLPH]] | +0.71 | +0.81 / +0.64 | both halves | 7e-06 |  |
| [[ZNF3]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTN3]] | -0.63 | -0.63 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-41.2, 2.5); signed map (-1.6, -21.2). **Vector** length 83.3, 18.9% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.9 | +11.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.9 | +4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.8 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +6.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +0.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, would explain all of this change | -2.8 | +0.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.8 | +3.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.5 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | +0.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | -1.3 | -1.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial rRNA methyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:2,234,195-2,242,205 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FJH1, RRMJ2; previously FTSJ2 |
| Gene groups (HGNC) | 7BS 2'O-ribose DNA/RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 4 pathways, smallest: rRNA modification in the mitochondrion; rRNA processing in the mitochondrion; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UI43](https://www.uniprot.org/uniprotkb/Q9UI43) (rRNA methyltransferase 2, mitochondrial):

> S-adenosyl-L-methionine-dependent 2'-O-ribose methyltransferase that catalyzes the formation of 2'-O-methyluridine at position 1369 (Um1369) in the 16S mitochondrial large subunit ribosomal RNA (mtLSU rRNA), a universally conserved modification in the peptidyl transferase domain of the mtLSU rRNA. This activity may require prior 2'-O-methylguanosine modification at position 1370 (Gm1370) by MRM3. Essential for late-stage assembly of the mitochondrial large ribosomal subunit (mt-LSU), which is …

**Summary**, from NCBI Gene [29960](https://www.ncbi.nlm.nih.gov/gene/29960):

> The protein encoded by this gene is a member of the S-adenosylmethionine-binding protein family. It is a nucleolar protein and it may be involved in the processing and modification of rRNA. This gene has been suggested to be involved in cell cycle control and DNA repair. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16352](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16352) · Entrez [29960](https://www.ncbi.nlm.nih.gov/gene/29960) · UniProt [Q9UI43](https://www.uniprot.org/uniprotkb/Q9UI43) · Ensembl [ENSG00000122687](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122687)

## Data

Gene col 4364: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4364); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4364, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4364]; `tensor/DDL_lfc|DDL_z.npy` [4364]; `embed/gene_vectors.npy` [4364]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4364 or target_col == 4364). Every well: [[MRM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
