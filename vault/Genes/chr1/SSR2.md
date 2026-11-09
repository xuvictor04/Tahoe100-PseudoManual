---
symbol: "SSR2"
type: "gene"
col: 8697
ensembl_id: "ENSG00000163479"
name: "signal sequence receptor subunit 2"
location: "1q22"
module: 49
arm: "+"
pooled_cpm: 94.37
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 7
n_dd_up_clean: 0
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SSR2

*signal sequence receptor subunit 2* — 1q22

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.390× (z -16.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACBD3]] (+0.84, fdr 7e-06), [[SEC61B]] (+0.84, fdr 7e-06), [[GORASP2]] (+0.82, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8697.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +5.1 | 2e-04 | 1/50 (HepG2/C3A) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | 1.34× | +3.6 | 0.10 | 29/47 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | 1.61× | +3.0 | 0.46 | 24/48 (SW480, SW1417, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8697.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.390×** | -16.3 | 0e+00 | 48/48 (NCI-H2030, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.581×** | -6.6 | 1e-08 | 36/48 (NCI-H2347, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.594×** | -6.1 | 2e-07 | 36/48 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.777×** | -4.3 | 0.002 | 35/48 (SNU-1, H4, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.710×** | -4.2 | 0.003 | 30/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.715×** | -3.9 | 0.008 | 32/48 (H4, SW 1271, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.733×** | -3.8 | 0.012 | 29/48 (hTERT-HPNE, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.765× | -3.0 | 0.17 | 23/45 (NCI-H23, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~5% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8697. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 159 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -17.3) |
| [[KATO III (line)]] | alt | 91.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -13.7) |
| [[A-172 (line)]] | wt | 129 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -15.2) |
| [[A-427 (line)]] | wt | 82.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -11.6) |
| [[HS-578T (line)]] | alt | 93.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 181 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -22.3) |
| [[NCI-H2347 (line)]] | alt | 109 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -20.3) |
| [[NCI-H460 (line)]] | wt | 111 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -15.4) |
| [[SHP-77 (line)]] | alt | 218 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -13.1) |
| [[SNU-1 (line)]] | wt | 54.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0842× (z -21.3) |
| [[SW 900 (line)]] | alt | 147 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -13.8) |
| [[SW48 (line)]] | wt | 89.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -12.0) |
| [[A549 (line)]] | wt | 70.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 90.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -13.1) |
| [[C-33 A (line)]] | alt | 54.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 95.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -15.5) |
| [[H4 (line)]] | wt | 132 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -16.3) |
| [[HCT15 (line)]] | alt | 93.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change |
| [[HOP62 (line)]] | alt | 95.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -10.2) |
| [[Hs 766T (line)]] | wt | 115 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -9.9) |
| [[HT-29 (line)]] | alt | 91.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -12.7) |
| [[hTERT-HPNE (line)]] | wt | 110 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -13.6) |
| [[J82 (line)]] | alt | 61.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -13.1) |
| [[LS 180 (line)]] | wt | 89.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.460× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 87.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.477× (z -9.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[NCI-H1792 (line)]] | alt | 93.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -9.4) |
| [[NCI-H661 (line)]] | alt | 49.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 61.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -12.2) |
| [[PANC-1 (line)]] | alt | 80.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -12.8) |
| [[RKO (line)]] | wt | 89.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -14.0) |
| [[RPMI-7951 (line)]] | alt | 114 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -12.9) |
| [[SNU-423 (line)]] | alt | 47.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -11.7) |
| [[SW1417 (line)]] | alt | 69.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -11.5) |
| [[SW480 (line)]] | alt | 65.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -15.8) |
| [[AN3 CA (line)]] | alt | 100 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 98.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 75.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 65.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8697), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACBD3]] | +0.84 | +0.81 / +0.80 | both halves | 7e-06 |  |
| [[SEC61B]] | +0.84 | +0.79 / +0.84 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 996 |
| [[GORASP2]] | +0.82 | +0.84 / +0.69 | both halves | 7e-06 |  |
| [[PDIA5]] | +0.81 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[MYDGF]] | +0.80 | +0.77 / +0.84 | both halves | 7e-06 |  |
| [[BET1L]] | +0.79 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[TMED9]] | +0.79 | +0.80 / +0.74 | both halves | 7e-06 |  |
| [[ERLEC1]] | +0.78 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[COG3]] | +0.78 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[HM13]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 | STRING 600 |
| [[GMPPA]] | +0.77 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[TXNDC11]] | +0.77 | +0.76 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2B]] | B | TOP2B activity raises SSR2's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.876). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.0, -34.4); signed map (-50.3, 11.3). **Vector** length 123, 43.5% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *XBP1(S) activates chaperone genes* (reactome, mean cos +0.64 to 8); *IRE1alpha activates chaperones* (reactome, mean cos +0.64 to 8); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.64 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | -1.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | -1.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.9 | +2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | +0.4 |
|  | [[EX229 (drug)]] 0.5 µM |  | +2.6 | +2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.6 | +2.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | -0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.0 | -0.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.6 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -3.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | -16.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -4.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.7 | -2.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | signal sequence receptor subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:156,009,048-156,020,951 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TLAP, TRAPB |
| Gene groups (HGNC) | Translocon associated protein complex subunits |
| Reactome | 2 pathways, smallest: Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [P43308](https://www.uniprot.org/uniprotkb/P43308) (Translocon-associated protein subunit beta):

> TRAP proteins are part of a complex whose function is to bind calcium to the ER membrane and thereby regulate the retention of ER resident proteins.

**Summary**, from NCBI Gene [6746](https://www.ncbi.nlm.nih.gov/gene/6746):

> The signal sequence receptor (SSR) is a glycosylated endoplasmic reticulum (ER) membrane receptor associated with protein translocation across the ER membrane. The SSR consists of 2 subunits, a 34-kD glycoprotein (alpha-SSR or SSR1) and a 22-kD glycoprotein (beta-SSR or SSR2). The human beta-signal sequence receptor gene (SSR2) maps to chromosome bands 1q21-q23. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11324](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11324) · Entrez [6746](https://www.ncbi.nlm.nih.gov/gene/6746) · UniProt [P43308](https://www.uniprot.org/uniprotkb/P43308) · Ensembl [ENSG00000163479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163479)

## Data

Gene col 8697: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8697); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8697, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8697]; `tensor/DDL_lfc|DDL_z.npy` [8697]; `embed/gene_vectors.npy` [8697]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8697 or target_col == 8697). Every well: [[SSR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
