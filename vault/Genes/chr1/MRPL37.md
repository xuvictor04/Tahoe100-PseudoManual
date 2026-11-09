---
symbol: "MRPL37"
type: "gene"
col: 3779
ensembl_id: "ENSG00000116221"
name: "mitochondrial ribosomal protein L37"
location: "1p32.3"
module: 72
arm: "+"
pooled_cpm: 30.8
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/072", "written"]
generated_by: "tahoemap"
---

# MRPL37

*mitochondrial ribosomal protein L37* — 1p32.3

> [!summary] In one line
> MRPL37 encodes mL37, a nuclear-encoded structural protein of the large subunit of the mitochondrial ribosome.

## What it is

The mitoribosome translates the thirteen OXPHOS subunits encoded by mitochondrial DNA; all of its own protein components are encoded in the nucleus and imported. MRPL37 is one of them, a constituent of the large (39S) subunit, placed in the structure by the cryo-EM work that resolved the human mitoribosome and associated with the inner membrane where translation is coupled to membrane insertion. It belongs to the mL37/mL65 family, proteins with no bacterial counterpart. Beyond structural placement and RNA binding its individual contribution is not separately characterised, and vendor claims of mitochondrial-disease association are not backed by a primary study I can cite. The gene is at 1p32.3.

## What is uncertain

Whether MRPL37 carries information of its own is doubtful. Mitoribosome subunits move as one tightly co-regulated module, so a slope on MRPL37 is effectively a slope on mitochondrial biogenesis, nearly collinear with dozens of other MRPL and MRPS genes — which is also the most economical explanation for its repression-arm membership, since arrest lowers biosynthetic capacity generally. No p53 response element at the locus has been reported, and p53's reported effects on mitochondrial biogenesis run in both directions, so even the expected sign is not secure.

## References

- Brown et al., 2014, Science — structure of the large subunit of the human mitochondrial ribosome, resolving its protein complement.
- Amunts et al., 2015, Science — structure of the complete human mitoribosome.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.46× (z +10.2, q 9e-22, up in 38 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 1.45× (z +4.2, q 0.003, up in 27 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.377×); [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.211×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.150×; ⚠ toxic; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BABAM1]] (+0.62, fdr 7e-06), [[MRPS15]] (+0.61, fdr 7e-06), [[INVS]] (+0.59, fdr 1e-05); moves opposite to [[JUNB]] (-0.52, fdr 2e-04), [[IER2]] (-0.52, fdr 3e-05), [[SKIL]] (-0.49, fdr 2e-04).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IER3]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Bendamustine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3779.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.46×** | +10.2 | 9e-22 | 38/45 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.14×** | +8.3 | 2e-14 | 34/38 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.54×** | +4.9 | 2e-04 | 29/45 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +4.2 | 0.003 | 27/48 (H4, HOP62, …) | two highest doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.47×** | +4.2 | 0.003 | 26/48 (SNU-423, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.61×** | +4.1 | 0.003 | 26/43 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.29×** | +4.1 | 0.003 | 24/47 (A549, NCI-H2347, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.51×** | +4.1 | 0.003 | 27/48 (NCI-H2030, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.9 | 0.007 | 23/45 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.014 | 25/48 (H4, NCI-H23, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.1 | 0.087 | 1/48 (SW 1088) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3779.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (MIA PaCa-2 0.377×); [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.211×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.150×; ⚠ toxic; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.813× | -3.3 | 0.56 | 22/47 (MIA PaCa-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3779. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 39.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -11.0) |
| [[A498 (line)]] | wt | 45.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H460 (line)]] | wt | 26.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.00× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[BT-474 (line)]] | alt | 21.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.150× (z -10.3) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 34.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1792 (line)]] | alt | 21.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.18× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[Panc 03.27 (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.211× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[PANC-1 (line)]] | alt | 38.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SNU-423 (line)]] | alt | 26.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.70× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[A-172 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 48.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 35.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3779), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BABAM1]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[MRPS15]] | +0.61 | +0.66 / +0.64 | both halves | 7e-06 | same gene group; pathway: Mitochondrial ribosome-associated quality control; STRING 924 |
| [[INVS]] | +0.59 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[PHB2]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SNX13]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[NAGPA]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[KIAA1143]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[LINC00630]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[UBE4B]] | +0.57 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[CLPP]] | +0.57 | +0.36 / +0.63 | both halves | 9e-05 |  |
| [[TRMT2A]] | +0.56 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[TNPO3]] | +0.56 | +0.31 / +0.58 | both halves | 2e-04 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUNB]] | -0.52 | -0.32 / -0.59 | both halves | 2e-04 |  |
| [[IER2]] | -0.52 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[SKIL]] | -0.49 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[CSRNP1]] | -0.48 | -0.38 / -0.51 | both halves | 7e-05 |  |
| [[IER3]] | -0.48 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[LMNA]] | -0.47 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[BCL3]] | -0.46 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[LINC02901]] | -0.46 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[SERPINB9]] | -0.46 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[SOCS2]] | -0.45 | -0.44 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IER3]] | B | IER3 activity lowers MRPL37's level | lines that do not express IER3 (5) vs lines expressing it (45) | 1.41× higher at baseline in the lines without IER3 | 0.041 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[PSMB5]] | B | PSMB5 activity lowers MRPL37's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bendamustine (drug)]] 0.5 µM | C | MRPL37's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | MRPL37's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.478 over the table, 0.087 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.539). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.3, -12.0); signed map (-21.7, -24.1). **Vector** length 53.1, 10.7% of its response variance represented; |z| ≥ 3 in 513 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +3.8 | +3.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.4 | +4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +4.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.9 | +2.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +1.3 | +1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.3 | -0.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.2 | +1.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.1 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -2.1 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.9 | -0.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -0.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -0.9 | -0.1 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | -0.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L37 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:54,184,041-54,225,464 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPML2, MRP-L2, mL37 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9BZE1](https://www.uniprot.org/uniprotkb/Q9BZE1) carries no function annotation.

**Summary**, from NCBI Gene [51253](https://www.ncbi.nlm.nih.gov/gene/51253):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14034](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14034) · Entrez [51253](https://www.ncbi.nlm.nih.gov/gene/51253) · UniProt [Q9BZE1](https://www.uniprot.org/uniprotkb/Q9BZE1) · Ensembl [ENSG00000116221](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116221)

## Data

Gene col 3779: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3779); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3779, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3779]; `tensor/DDL_lfc|DDL_z.npy` [3779]; `embed/gene_vectors.npy` [3779]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3779 or target_col == 3779). Every well: [[MRPL37 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/MRPL37.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
