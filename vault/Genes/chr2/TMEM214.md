---
symbol: "TMEM214"
type: "gene"
col: 4118
ensembl_id: "ENSG00000119777"
name: "transmembrane protein 214"
location: "2p23.3"
module: 42
arm: "+"
pooled_cpm: 44.98
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 15
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# TMEM214

*transmembrane protein 214* — 2p23.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.645× (z -7.1, q 7e-10, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPG1]] (+0.77, fdr 7e-06), [[SRPRA]] (+0.77, fdr 7e-06), [[SSR1]] (+0.74, fdr 7e-06); moves opposite to [[SPPL3]] (-0.55, fdr 7e-05), [[JMJD1C]] (-0.54, fdr 2e-05), [[TBCA]] (-0.52, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[XRK3F2 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4118.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.35× | +3.5 | 0.26 | 20/48 (CFPAC-1, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4118.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.645×** | -7.1 | 7e-10 | 31/47 (HS-578T, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.664×** | -6.6 | 1e-08 | 38/48 (SNU-1, AsPC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.603×** | -6.2 | 1e-07 | 34/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.626×** | -5.7 | 2e-06 | 33/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.753×** | -4.8 | 2e-04 | 35/48 (SNU-1, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **0.766×** | -4.4 | 0.001 | 29/48 (SNU-423, A-427, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.720×** | -4.0 | 0.005 | 28/48 (hTERT-HPNE, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.723×** | -4.0 | 0.005 | 23/48 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.729×** | -3.7 | 0.013 | 24/48 (C-33 A, NCI-H2030, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.745×** | -3.6 | 0.018 | 25/48 (KATO III, SW 1088, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.750×** | -3.5 | 0.023 | 22/48 (SNU-1, Hs 766T, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.759×** | -3.4 | 0.035 | 25/48 (SNU-1, HepG2/C3A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.755×** | -3.3 | 0.040 | 24/47 (hTERT-HPNE, SW 1271, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.770×** | -3.2 | 0.056 | 23/48 (A-172, KATO III, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.766×** | -3.1 | 0.065 | 23/48 (H4, HOP62, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4118. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 46.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.429× (z -9.2) |
| [[H4 (line)]] | wt | 46.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0801× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.274× (z -10.1) |
| [[SNU-1 (line)]] | wt | 51.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -11.0) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -9.5) |
| [[A-427 (line)]] | wt | 36.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.290× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~53% of this change |
| [[AN3 CA (line)]] | alt | 30.7 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0816× (z -9.3) |
| [[COLO 205 (line)]] | alt | 44.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 64.3 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.246× (z -8.9) |
| [[HS-578T (line)]] | alt | 65.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -11.6) |
| [[J82 (line)]] | alt | 35.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 50.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change |
| [[NCI-H1792 (line)]] | alt | 38.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 28.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -11.4) |
| [[RPMI-7951 (line)]] | alt | 80.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 37.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -11.2) |
| [[SW 1088 (line)]] | alt | 62.9 | 0 | 1 | — | [[Meloxicam (drug)]] 0.05 µM 0.0608× (z -8.5) |
| [[A-172 (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 85.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 48.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4118), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPG1]] | +0.77 | +0.82 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SRPRA]] | +0.77 | +0.78 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SSR1]] | +0.74 | +0.73 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SEC61A1]] | +0.72 | +0.80 / +0.64 | both halves | 7e-06 | STRING 778 |
| [[GMPPB]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[LRRC59]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[B4GALT7]] | +0.70 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[GMPPA]] | +0.67 | +0.75 / +0.54 | both halves | 1e-05 | STRING 465 |
| [[STT3A]] | +0.66 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[TMED2]] | +0.66 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[SLC39A7]] | +0.65 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[MANF]] | +0.64 | +0.74 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPPL3]] | -0.55 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[JMJD1C]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[TBCA]] | -0.52 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[GPATCH8]] | -0.52 | -0.60 / -0.37 | both halves | 8e-05 |  |
| [[WBP4]] | -0.51 | -0.58 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[XRK3F2 (drug)]] 5 µM | C | TMEM214's natural level raises the cells' numbers under XRK3F2 5 µM (protects the cells) | TMEM214's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.327 over the table, 0.071 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.1, -29.7); signed map (-55.8, 8.8). **Vector** length 107, 29.8% of its response variance represented; |z| ≥ 3 in 737 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.55 to 11); *Unfolded Protein Response (UPR)* (reactome, mean cos +0.53 to 9); *IRE1alpha activates chaperones* (reactome, mean cos +0.56 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +5.0 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | +4.6 | -1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.9 | -1.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | -0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +3.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +1.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.1 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -0.7 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.0 | +1.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -4.7 | -3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.2 | -3.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.8 | -4.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -2.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.5 | -3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -2.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.6 | -2.7 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -2.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 214 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:27,032,910-27,041,694 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20254 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6NUQ4](https://www.uniprot.org/uniprotkb/Q6NUQ4) (Transmembrane protein 214):

> Critical mediator, in cooperation with CASP4, of endoplasmic reticulum-stress induced apoptosis. Required or the activation of CASP4 following endoplasmic reticulum stress.

**Summary**, from NCBI Gene [54867](https://www.ncbi.nlm.nih.gov/gene/54867):

> Predicted to be involved in apoptotic process. Located in cytoplasmic microtubule and endoplasmic reticulum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25983](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25983) · Entrez [54867](https://www.ncbi.nlm.nih.gov/gene/54867) · UniProt [Q6NUQ4](https://www.uniprot.org/uniprotkb/Q6NUQ4) · Ensembl [ENSG00000119777](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119777)

## Data

Gene col 4118: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4118); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4118, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4118]; `tensor/DDL_lfc|DDL_z.npy` [4118]; `embed/gene_vectors.npy` [4118]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4118 or target_col == 4118). Every well: [[TMEM214 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM214.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
