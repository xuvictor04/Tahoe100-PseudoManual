---
symbol: "PFDN5"
type: "gene"
col: 4423
ensembl_id: "ENSG00000123349"
name: "prefoldin subunit 5"
location: "12q13.13"
module: 43
arm: "+"
pooled_cpm: 44.09
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/043"]
generated_by: "tahoemap"
---

# PFDN5

*prefoldin subunit 5* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.21× (z +7.7, q 7e-12, up in 34 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.51× (z +4.1, q 0.004, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.741× (z -4.3, q 0.010, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPLP1]] (+0.81, fdr 7e-06), [[RPS20]] (+0.80, fdr 7e-06), [[RPL34]] (+0.79, fdr 7e-06).
> It sits in the **+** arm of [[Module 043]] (Eukaryotic Translation Elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4423.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.21×** | +7.7 | 7e-12 | 34/40 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +7.5 | 1e-11 | 43/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.70×** | +5.4 | 1e-05 | 41/46 (SW 900, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +5.1 | 6e-05 | 32/45 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +4.1 | 0.004 | 35/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +3.9 | 0.011 | 34/48 (PANC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.42×** | +3.6 | 0.027 | 28/47 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.027 | 34/48 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.4 | 0.044 | 30/47 (MIA PaCa-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4423.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.741×** | -4.3 | 0.010 | 31/48 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.702× | -3.6 | 0.10 | 26/47 (MIA PaCa-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4423. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 47.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +8.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 41.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 55.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.46× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 64.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4423), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 19 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPLP1]] | +0.81 | +0.79 / +0.78 | both halves | 7e-06 | STRING 482 |
| [[RPS20]] | +0.80 | +0.77 / +0.78 | both halves | 7e-06 | STRING 649 |
| [[RPL34]] | +0.79 | +0.80 / +0.77 | both halves | 7e-06 | STRING 568 |
| [[UBA52]] | +0.79 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[RPL13A]] | +0.78 | +0.80 / +0.77 | both halves | 7e-06 | STRING 495 |
| [[RPL30]] ⚠ | +0.78 | +0.68 / +0.81 | both halves | 7e-06 | STRING 661; ⚠ in the vector space only through flagged drug-doses |
| [[RPL35A]] | +0.78 | +0.79 / +0.74 | both halves | 7e-06 | STRING 562 |
| [[RPL31]] | +0.78 | +0.78 / +0.74 | both halves | 7e-06 | STRING 863 |
| [[RPL19]] | +0.78 | +0.72 / +0.77 | both halves | 7e-06 | STRING 506 |
| [[COX7C]] | +0.77 | +0.75 / +0.71 | both halves | 7e-06 | STRING 542 |
| [[NENF]] | +0.77 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[RPS14]] | +0.77 | +0.82 / +0.72 | both halves | 7e-06 | STRING 419 |
| [[RPS27]] | +0.77 | +0.77 / +0.74 | both halves | 7e-06 | STRING 482 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers PFDN5's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 043]] — Eukaryotic Translation Elongation; 103 genes; this gene is in the **+** arm (projection on the module's main direction 0.807). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (-44.3, -28.6); signed map (-59.2, -5.6). **Vector** length 69.9, 19.6% of its response variance represented; |z| ≥ 3 in 482 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.69 to 55); *Peptide chain elongation* (reactome, mean cos +0.70 to 52); *Formation of a pool of free 40S subunits* (reactome, mean cos +0.70 to 53).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +3.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.5 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.2 | +2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.9 | +1.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.7 | +0.9 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +1.5 | -0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | -1.2 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.6 | -0.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | prefoldin subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,295,291-53,299,452 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PFD5, MM-1 |
| Gene groups (HGNC) | Prefoldin subunits |
| Reactome | 4 pathways, smallest: Prefoldin mediated transfer of substrate  to CCT/TriC; Cooperation of Prefoldin and TriC/CCT  in actin and tubulin folding; Chaperonin-mediated protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99471](https://www.uniprot.org/uniprotkb/Q99471) (Prefoldin subunit 5):

> Binds specifically to cytosolic chaperonin (c-CPN) and transfers target proteins to it. Binds to nascent polypeptide chain and promotes folding in an environment in which there are many competing pathways for nonnative proteins. Represses the transcriptional activity of MYC.

**Summary**, from NCBI Gene [5204](https://www.ncbi.nlm.nih.gov/gene/5204):

> This gene encodes a member of the prefoldin alpha subunit family. The encoded protein is one of six subunits of prefoldin, a molecular chaperone complex that binds and stabilizes newly synthesized polypeptides, thereby allowing them to fold correctly. The complex, consisting of two alpha and four beta subunits, forms a double beta barrel assembly with six protruding coiled-coils. The encoded protein may also repress the transcriptional activity of the proto-oncogene c-Myc. Alternatively spliced …

**Accessions** — [HGNC:8869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8869) · Entrez [5204](https://www.ncbi.nlm.nih.gov/gene/5204) · UniProt [Q99471](https://www.uniprot.org/uniprotkb/Q99471) · Ensembl [ENSG00000123349](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123349)

## Data

Gene col 4423: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4423); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4423, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4423]; `tensor/DDL_lfc|DDL_z.npy` [4423]; `embed/gene_vectors.npy` [4423]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4423 or target_col == 4423). Every well: [[PFDN5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PFDN5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
